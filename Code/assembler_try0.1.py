# CPU-Spezifikation
OPCODES = {"AND(D,A)": 000000, "0": 000010, "OR(D,A)": 000100,
            "XOR":001000, "NEG(D)": 001100,
            "NEG(A)": 001101, "-1": 001110, "D + A": 010000,"D - A": 010100,
            "A - D": 010101, "-A": 010110, "-D": 010111, "D + 1": 011000,
            "A + 1": 011001, "1": 011010, "D - 1": 011100, "A - 1": 011101,
            "AND(D,M)": 100000, "OR(D,M)": 100100, "XOR(D,M)": 101000,
            "NEG(M)": 101101, "D + M": 110000, "D - M": 110100, "M - D": 110101,
            "-M": 110110, "M + 1": 111001, "M - 1": 111101}
Ziel = {"dw": 000, "wM": 001, "wD": 010, 
        "wA": 100, "wDM": 011, "wAM": 101, 
        "wAD": 110, "wADM": 111}
Jump = {"no jump": 000, "comp>0": 001, "comp=0": 010, "comp>=0": 011,
        "comp<0": 100, "comp/=0": 101, "comp=<0": 110, "comp always": 111}
REGISTERS = {"A": 000110, "D": 000111, "M": 100110}

def translate_line(line):
    # Beispiel-Eingabe: "AND R1, R2"
    parts = line.replace(",", "").split()
    cmd, direction, target = parts[0], parts[1], parts[2]
    
    # Bits zusammenbauen: Opcode (4 Bit) + Reg1 (2 Bit) + Reg2 (2 Bit)
    instruction = ("0b" + OPCODES[cmd] + REGISTERS[direction] + REGISTERS[target])
    return instruction # Liefert eine 16-Bit-Zahl
