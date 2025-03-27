
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class LZ77 {

    public static void compress(File inputFile, File outputFile, int windowSize, int maxMatchLength) throws IOException {
        byte[] data = readAllBytes(inputFile);
        List<Token> tokens = new ArrayList<>();
        int currentPos = 0;

        while (currentPos < data.length) {
            int maxMatch = 0;
            int bestDistance = 0;
            int startWindow = Math.max(0, currentPos - windowSize);
            int maxPossibleLength = Math.min(maxMatchLength, data.length - currentPos - 1);

            if (maxPossibleLength < 0) {
                maxPossibleLength = data.length - currentPos;
            }

            for (int start = startWindow; start < currentPos; start++) {
                int currentLength = 0;
                while (currentLength < maxPossibleLength &&
                        start + currentLength < currentPos &&
                        currentPos + currentLength < data.length &&
                        data[start + currentLength] == data[currentPos + currentLength]) {
                    currentLength++;
                }
                if (currentLength > maxMatch) {
                    maxMatch = currentLength;
                    bestDistance = currentPos - start;
                }
            }

            if (maxMatch > 0 && maxPossibleLength > 0) {
                int nextCharPos = currentPos + maxMatch;
                byte nextChar = nextCharPos < data.length ? data[nextCharPos] : 0;
                tokens.add(new Token(bestDistance, maxMatch, nextChar));
                currentPos += maxMatch + 1;
            } else {
                byte nextChar = data[currentPos];
                tokens.add(new Token(0, 0, nextChar));
                currentPos++;
            }
        }

        writeTokens(outputFile, data.length, tokens);
    }

    public static void decompress(File inputFile, File outputFile) throws IOException {
        try (DataInputStream dis = new DataInputStream(new FileInputStream(inputFile))) {
            byte[] magic = new byte[4];
            dis.readFully(magic);
            if (!new String(magic).equals("LZ77")) {
                throw new IOException("Invalid format");
            }

            int originalSize = dis.readInt();
            List<Byte> decompressed = new ArrayList<>();

            while (decompressed.size() < originalSize) {
                if (dis.available() < 4) break;

                int distance = dis.readShort() & 0xFFFF;
                int length = dis.readByte() & 0xFF;
                byte nextChar = dis.readByte();

                if (length > 0) {
                    int start = decompressed.size() - distance;
                    if (start < 0) throw new IOException("Invalid distance");
                    for (int i = 0; i < length; i++) {
                        decompressed.add(decompressed.get(start + i));
                    }
                }
                decompressed.add(nextChar);
            }

            if (decompressed.size() != originalSize) {
                throw new IOException("Size mismatch");
            }

            try (OutputStream os = new FileOutputStream(outputFile)) {
                for (byte b : decompressed) {
                    os.write(b);
                }
            }
        }
    }

    private static byte[] readAllBytes(File file) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        try (InputStream in = new FileInputStream(file)) {
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = in.read(buffer)) != -1) {
                baos.write(buffer, 0, bytesRead);
            }
        }
        return baos.toByteArray();
    }

    private static void writeTokens(File outputFile, int dataLength, List<Token> tokens) throws IOException {
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(outputFile))) {
            dos.writeBytes("LZ77");
            dos.writeInt(dataLength);
            for (Token token : tokens) {
                dos.writeShort(token.distance);
                dos.writeByte(token.length);
                dos.writeByte(token.nextChar);
            }
        }
    }

    private static class Token {
        int distance;
        int length;
        byte nextChar;

        Token(int distance, int length, byte nextChar) {
            this.distance = distance;
            this.length = length;
            this.nextChar = nextChar;
        }
    }

    public static void main(String[] args) {
        if (args.length < 5) {
            System.out.println("Usage: java LZ77 <compress|decompress> <inputFile> <outputFile> <windowSize> <maxMatchLength>");
            return;
        }

        String mode = args[0];
        File inputFile = new File(args[1]);
        File outputFile = new File(args[2]);
        int windowSize = Integer.parseInt(args[3]);
        int maxMatchLength = Integer.parseInt(args[4]);

        try {
            if (mode.equals("compress")) {
                compress(inputFile, outputFile, windowSize, maxMatchLength);
                System.out.println("Compression completed successfully.");
            } else if (mode.equals("decompress")) {
                decompress(inputFile, outputFile);
                System.out.println("Decompression completed successfully.");
            } else {
                System.out.println("Invalid mode. Use 'compress' or 'decompress'.");
            }
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
