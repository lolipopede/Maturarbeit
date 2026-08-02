# CPU-Spezifikation
OPCODES = {"AND(D,A)": 0b000000, "0": 0b000010, "OR(D,A)": 0b000100,
            "XOR":0b001000, "NEG(D)": 0b001100,
            "NEG(A)": 0b001101, "-1": 0b001110, "D+A": 0b010000,"D-A": 0b010100,
            "A-D": 0b010101, "-A": 0b010110, "-D": 0b010111, "D+1": 0b011000,
            "A+1": 0b011001, "1": 0b011010, "D-1": 0b011100, "A-1": 0b011101,
            "AND(D,M)": 0b100000, "OR(D,M)": 0b100100, "XOR(D,M)": 0b101000,
            "NEG(M)": 0b101101, "D+M": 0b110000, "D-M": 0b110100, "M-D": 0b110101,
            "-M": 0b110110, "M+1": 0b111001, "M-1": 0b111101}
Ziel = {"dw": 0b000, "wM": 0b001, "wD": 0b010, 
        "wA": 0b100, "wDM": 0b011, "wAM": 0b101, 
        "wAD": 0b110, "wADM": 0b111}
Jump = {"nj": 0b000, "comp>0": 0b001, "comp=0": 0b010, "comp>=0": 0b011,
        "comp<0": 0b100, "comp/=0": 0b101, "comp=<0": 0b110, "comp always": 0b111}
REGISTERS = {"A": 0b000110, "D": 0b000111, "M": 0b100110}

def translate_line(line):
    # Beispiel-Eingabe: "AND R1, R2"
    parts = line.replace(",", " ").split()
    cmd, direction, target = parts[0], parts[1], parts[2]
    
    # Bits zusammenbauen: Opcode (4 Bit) + Reg1 (2 Bit) + Reg2 (2 Bit)
    instruction = "0b1111" + format(OPCODES[cmd], "06b") + format(Ziel[direction], "03b") + format(Jump[target], "03b")
    print(instruction)# Liefert eine 16-Bit-Zahl
   


with open(r"C:\Users\kogog\OneDrive\Maturarbeit\Code\test_for_assembler.txt", "r", encoding="utf-8") as datei:
    inhalt = datei.read()
    translated_lines = [translate_line(line) for line in inhalt.splitlines() if line.strip()]
    datei.close()

