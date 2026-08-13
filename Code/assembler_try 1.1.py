# CPU-Spezifikation
from pathlib import Path
import re

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


def encode_alpha_instruction(value):
    if value < 0:
        raise ValueError("Alpha-Befehl darf nur positive Zahlen enthalten.")
    if value >= 2 ** 15:
        raise ValueError("Alpha-Befehl passt nicht in 15 Bit.")
    return "0b" + "0" + format(value, "015b")

def translate_line(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    alpha_match = re.fullmatch(r"A\s*=\s*(\d+)", line, flags=re.IGNORECASE)
    if alpha_match:
        value = int(alpha_match.group(1))
        return encode_alpha_instruction(value)
    
    parts = line.replace(",", " ").split()
    cmd, direction, target = parts[0], parts[1], parts[2]
    if cmd not in OPCODES:
        raise ValueError(f"Unbekannter Opcode: {cmd}")
    if direction not in Ziel:
        raise ValueError(f"Unbekanntes Ziel: {direction}")
    if target not in Jump:
        raise ValueError(f"Unbekannter Jump: {target}")    

    instruction = "0b1111" + format(OPCODES[cmd], "06b") + format(Ziel[direction], "03b") + format(Jump[target], "03b")
    return instruction
   

def main():
    input_path = Path(__file__).with_name("test_for_assembler.asm")
    with input_path.open("r", encoding="utf-8") as datei:
        inhalt = datei.read()

    for line in inhalt.splitlines():
        translated = translate_line(line)
        if translated is not None:
            print(translated)


if __name__ == "__main__":
    main()
