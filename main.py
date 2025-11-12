from models import run_readability_analysis


def main():
    exit_key = 1

    while exit_key:
        print("[- IN THIS PROGRAM YOU COULD TRY MODEL PREDICTION -]")
        print("[", "-" * 100, "]")
        print("[-INPUT YOUR TEXT HERE-]")
        print("[-MODEL-] << ", end="")

        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        
        text_content = "\n".join(lines)
        
        results = run_readability_analysis(text_content)

        print("[", "-" * 100, "]")
        print("[-YOUR METRICS-]")
        print("[-MODEL-] >> ")
        print("[-Predicted level-]", results[0])
        print("[-Total words-]", results[1])
        print("[-Total sentences-]", results[2])
        print("[-Average sentence length-]", results[3])
        print("[-Average word length-]", results[4])
        print("[-Word sentence difference-]", results[5])
        print("[-Vocabulary richness-]", results[6])
        print("[-Syllables per word-]", results[7])
        print("[-Noun percentage-]", results[8])
        print("[-Verb percentage-]", results[9])
        print("[-Adjective percentage-]", results[10])
        print("[-Complex conjunctions frequency-]", results[11])
        print("[-Punctuation density-]", results[12])
        print("[-Flesch reading ease-]", results[13])
        print("[-Dale-Chall readability score-]", results[14])
        print("[-SMOG index-]", results[15])
        print("[-Automated readability index-]", results[16])
        print("[-Coleman-Liau index-]", results[17])
        print("[-Gunning fog index-]", results[18])
        print("[", "-" * 100, "]")
        print("[-ENTER 0 TO EXIT OR 1 TO CONTINUE-] << ", end="")
        exit_key = int(input())


if __name__ == '__main__':
    main()
