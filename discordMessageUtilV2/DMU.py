import os


# ========== DISCORD MESSAGE SPLITTER TOOL: For all your discord RP needs! ==========
# This script splits long text messages into smaller chunks that are
# Discord-friendly (under 2000 characters, 4000 for nitro users), with an optional output
# to output direct to console or file.
# Written by ATR2400
# 2025/07/11
# ==================================================

MAXCHARS = 1950
BREAK_MARK = "\n\n==== BREAK ====\n\n"


def main():

    
    print("=" * 50)
    print("         DISCORD MESSAGE SPLITTER TOOL")
    print("                 by ATR2400 (Kal!)")
    print("=" * 50)

    global MAXCHARS
    while True:
        nitro_input = input("\nDo you have Discord Nitro? (y/n): ").strip().lower()
        if nitro_input == 'y':
            MAXCHARS = 3950
            break
        elif nitro_input == 'n':
            MAXCHARS = 1950
            break
        else:
            print("[!] Please enter 'y' for yes or 'n' for no.")
            

    inputMode = select_mode(
        "Select text input method:",
        ["Paste in: Paste message directly into console",
         "File in: Select a .txt file containing your message"]
    )

    outputMode = select_mode(
        "Select output method:",
        ["Console out: Display split message here",
         "File out: Save message to a file in /outputs folder"]
    )

    output, err_code = handleInput(inputMode)
    if err_code:
        print(f"\n[!] Error: {err_code}")
        return

    err_code = handleOutput(outputMode, output)
    if err_code:
        print(f"\n[!] Error: {err_code}")
        return

    print("\n✅ Process complete!")
    if outputMode == 2:
        print("📁 Output saved to the 'outputs' folder.")
    print("=" * 50)

    input("press enter to exit...")

def select_mode(prompt_title, options):
    print(f"\n{prompt_title}\n")
    for idx, option in enumerate(options, 1):
        print(f"  {idx}. {option}")

    while True:
        try:
            selection = int(input("\nEnter your selection (1 or 2): ").strip())
            if selection in [1, 2]:
                return selection
            print("[!] Please choose either 1 or 2.")
        except ValueError:
            print("[!] Invalid input. Please enter 1 or 2.")


def handleInput(inputMode):
    err_code = None
    message = ""

    if inputMode == 1:
        print("\nPaste your Discord message below (press Enter when done):")
        message = input("> ")
    else:
        print("\n[📂] File selection: Enter the full path or drag in your text file.")
        while True:
            filePath = input("Enter file path (or type 'exit' to cancel): ").strip()
            filePath = filePath.strip('"')

            if filePath.lower() == "exit":
                return None, "User exited"

            try:
                with open(filePath, "r", encoding="utf-8", errors="ignore") as file:
                    message = file.read()
                break
            except FileNotFoundError:
                print("[!] File not found. Try again.")
            except Exception as e:
                print(f"[!] Error reading file: {e}")

    output = splitMessage(message)
    return output, err_code


def handleOutput(outputMode, output):
    err_code = None

    if outputMode == 1:
        print("\n===== OUTPUT START =====")
        print(output)
        print("====== OUTPUT END ======\n")
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, "outputs")
        os.makedirs(output_dir, exist_ok=True)

        while True:
            fileName = input("\nEnter output file name (or 'exit' to cancel): ").strip()

            if fileName.lower() == "exit":
                return "User exited"

            filePath = os.path.join(output_dir, fileName + ".txt")

            try:
                with open(filePath, "w", encoding="utf-8", errors="ignore") as file:
                    file.write(output)
                break
            except Exception as e:
                print(f"[!] Error writing to file: {e}")

    return err_code


def splitMessage(message):
    brokenMessage = ""
    messageBlock = ""
    blockCount = 0

    for char in message:
        if char == " " and blockCount > MAXCHARS:
            brokenMessage += messageBlock + BREAK_MARK
            messageBlock = ""
            blockCount = 0
        else:
            messageBlock += char
            blockCount += 1

    brokenMessage += messageBlock
    return brokenMessage


if __name__ == "__main__":
    main()
