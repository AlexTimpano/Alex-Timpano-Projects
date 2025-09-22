using System.Drawing.Text;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace DIscordMessageUtilV3
{
    public partial class Form1 : Form
    {
        private string inputPath = "";

        private const short NORMALLIMIT = 1950;
        private const short NITROLIMIT = 3950;
        private const string BREAK = "\n\n=====BREAK=====\n\n";

        public Form1()
        {
            InitializeComponent();

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void FileIn_CheckedChanged(object sender, EventArgs e)
        {
            if (FileIn.Checked)
            {
                textBox2.Visible = true;
                browseInput.Visible = true;
                TextInputBox.Visible = false;
            }
        }

        private void TextIn_CheckedChanged(object sender, EventArgs e)
        {
            if (TextIn.Checked)
            {
                textBox2.Visible = false;
                browseInput.Visible = false;
                TextInputBox.Visible = true;
            }
        }

        private void browseInput_Click(object sender, EventArgs e)
        {
            if (textInputDialogue.ShowDialog() == DialogResult.OK)
            {
                inputPath = textInputDialogue.FileName;
                textBox2.Text = inputPath;
            }

        }

        private void hasNitroButton_CheckedChanged(object sender, EventArgs e)
        {
            return;
        }

        private void SplitMessage_Click(object sender, EventArgs e)
        {

            string workingText;
            string outputText = "";
            short maxLength = hasNitroButton.Checked == false ? NORMALLIMIT : NITROLIMIT;
            short charCount = 0;
            StringBuilder sb = new StringBuilder();

            if (TextIn.Checked == true)
            {
                if (TextInputBox.Text == "")
                {
                    MessageBox.Show("No text input provided!", "Error: Could not split message", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                else
                {
                    workingText = TextInputBox.Text;
                }
            }

            else
            {
                if (inputPath == "")
                {
                    MessageBox.Show("No file selected", "Error: Could not split message", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
                else
                {
                    workingText = File.ReadAllText(inputPath);
                    if (workingText == "")
                    {
                        MessageBox.Show("No text input provided!", "Error: Could not split message", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        return;
                    }
                }
            }


            foreach (char c in workingText)
            {
                if (charCount >= maxLength && c == ' ')
                {
                    sb.Append(BREAK);
                    charCount= 0;
                }

                else
                {
                    sb.Append(c);
                    charCount++;
                }
            }

            outputText = sb.ToString();

            if (CopyOut.Checked == true)
            {
                OutputTextBox.Text= outputText;
            }

            else
            {
                if(textOutputDialogue.ShowDialog() == DialogResult.OK)
                {
                    string outputPath = textOutputDialogue.FileName;

                    try
                    {
                        File.WriteAllText(outputPath, outputText);
                        MessageBox.Show($"File saved successfully to {outputPath}", "Success!", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }

                    catch(Exception ex)
                    {
                        MessageBox.Show("Error saving to file: Are you sure you chose a valid file?", "Error: Could not save to file", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }


        }

        
    }
}
