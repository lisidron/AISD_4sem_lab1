import java.io.*;
import java.nio.file.Files;
import java.util.*;

public class LZ78 {
    static class ByteSequence {
        private final byte[] data;
        private final int hashCode;

        public ByteSequence(byte[] data) {
            this.data = data;
            this.hashCode = Arrays.hashCode(data);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            ByteSequence that = (ByteSequence) obj;
            return Arrays.equals(data, that.data);
        }

        @Override
        public int hashCode() {
            return hashCode;
        }
    }

    static class Compressor {
        public static void compress(File inputFile, File outputFile) throws IOException {
            byte[] data = Files.readAllBytes(inputFile.toPath());
            Map<ByteSequence, Integer> dictionary = new HashMap<>();
            List<byte[]> dictionaryList = new ArrayList<>();

            dictionary.put(new ByteSequence(new byte[0]), 0);
            dictionaryList.add(new byte[0]);

            List<Pair> outputPairs = new ArrayList<>();
            List<Byte> currentSequence = new ArrayList<>();

            for (byte b : data) {
                List<Byte> tempSequence = new ArrayList<>(currentSequence);
                tempSequence.add(b);
                ByteSequence tempSeq = new ByteSequence(toByteArray(tempSequence));
                if (dictionary.containsKey(tempSeq)) {
                    currentSequence = tempSequence;
                } else {
                    int currentIndex = dictionary.get(new ByteSequence(toByteArray(currentSequence)));
                    outputPairs.add(new Pair(currentIndex, b));
                    dictionary.put(tempSeq, dictionaryList.size());
                    dictionaryList.add(toByteArray(tempSequence));
                    currentSequence.clear();
                }
            }

            if (!currentSequence.isEmpty()) {
                int currentIndex = dictionary.get(new ByteSequence(toByteArray(currentSequence)));
                outputPairs.add(new Pair(currentIndex, (byte) 0));
            }

            try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(outputFile))) {
                for (Pair pair : outputPairs) {
                    dos.writeInt(pair.index);
                    dos.writeByte(pair.value);
                }
                dos.writeInt(-1);
                dos.writeByte(0);
            }
        }

        private static byte[] toByteArray(List<Byte> list) {
            byte[] array = new byte[list.size()];
            for (int i = 0; i < list.size(); i++) {
                array[i] = list.get(i);
            }
            return array;
        }

        static class Pair {
            int index;
            byte value;

            Pair(int index, byte value) {
                this.index = index;
                this.value = value;
            }
        }
    }

    static class Decompressor {
        public static void decompress(File inputFile, File outputFile) throws IOException {
            List<Byte> decompressedData = new ArrayList<>();
            List<byte[]> dictionary = new ArrayList<>();
            dictionary.add(new byte[0]);

            try (DataInputStream dis = new DataInputStream(new FileInputStream(inputFile))) {
                while (true) {
                    int index;
                    byte value;
                    try {
                        index = dis.readInt();
                        value = dis.readByte();
                    } catch (EOFException e) {
                        break;
                    }
                    if (index == -1) {
                        break;
                    }

                    if (index >= dictionary.size()) {
                        throw new IOException("Invalid index: " + index);
                    }

                    byte[] phrase = dictionary.get(index);
                    byte[] newEntry = Arrays.copyOf(phrase, phrase.length + 1);
                    newEntry[phrase.length] = value;
                    dictionary.add(newEntry);

                    for (byte b : newEntry) {
                        decompressedData.add(b);
                    }
                }
            }

            if (!decompressedData.isEmpty() && decompressedData.get(decompressedData.size() - 1) == 0) {
                decompressedData.remove(decompressedData.size() - 1);
            }

            byte[] result = new byte[decompressedData.size()];
            for (int i = 0; i < result.length; i++) {
                result[i] = decompressedData.get(i);
            }
            Files.write(outputFile.toPath(), result);
        }
    }

    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println("Использование: java LZ78SingleFile <режим> <входной файл> <выходной файл>");
            System.out.println("Режимы:");
            System.out.println("  compress   - сжатие файла");
            System.out.println("  decompress - распаковка файла");
            System.exit(1);
        }

        String mode = args[0];
        File inputFile = new File(args[1]);
        File outputFile = new File(args[2]);

        if (!inputFile.exists()) {
            System.err.println("Ошибка: входной файл не существует!");
            System.exit(1);
        }

        try {
            switch (mode) {
                case "compress":
                    Compressor.compress(inputFile, outputFile);
                    System.out.println("Сжатие завершено. Результат сохранен в " + outputFile.getPath());
                    break;
                case "decompress":
                    Decompressor.decompress(inputFile, outputFile);
                    System.out.println("Распаковка завершена. Результат сохранен в " + outputFile.getPath());
                    break;
                default:
                    System.err.println("Ошибка: неизвестный режим '" + mode + "'");
                    System.exit(1);
            }
        } catch (IOException e) {
            System.err.println("Ошибка ввода/вывода:");
            e.printStackTrace();
            System.exit(1);
        }
    }
}