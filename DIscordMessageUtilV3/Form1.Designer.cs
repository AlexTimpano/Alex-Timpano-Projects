namespace DIscordMessageUtilV3
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            InputBox = new GroupBox();
            TextIn = new RadioButton();
            FileIn = new RadioButton();
            OutputBox = new GroupBox();
            CopyOut = new RadioButton();
            FileOut = new RadioButton();
            SplitMessage = new Button();
            TextInputBox = new RichTextBox();
            OutputTextBox = new RichTextBox();
            textBox2 = new TextBox();
            browseInput = new Button();
            NitroBox = new GroupBox();
            lacksNitroButton = new RadioButton();
            hasNitroButton = new RadioButton();
            textInputDialogue = new OpenFileDialog();
            textOutputDialogue = new SaveFileDialog();
            InputBox.SuspendLayout();
            OutputBox.SuspendLayout();
            NitroBox.SuspendLayout();
            SuspendLayout();
            // 
            // InputBox
            // 
            InputBox.Controls.Add(TextIn);
            InputBox.Controls.Add(FileIn);
            InputBox.Location = new Point(90, 33);
            InputBox.Name = "InputBox";
            InputBox.Size = new Size(300, 150);
            InputBox.TabIndex = 0;
            InputBox.TabStop = false;
            InputBox.Text = "Select input mode";
            // 
            // TextIn
            // 
            TextIn.AutoSize = true;
            TextIn.Checked = true;
            TextIn.Location = new Point(16, 40);
            TextIn.Name = "TextIn";
            TextIn.Size = new Size(112, 29);
            TextIn.TabIndex = 1;
            TextIn.TabStop = true;
            TextIn.Text = "Paste text";
            TextIn.UseVisualStyleBackColor = true;
            TextIn.CheckedChanged += TextIn_CheckedChanged;
            // 
            // FileIn
            // 
            FileIn.AutoSize = true;
            FileIn.Location = new Point(16, 94);
            FileIn.Name = "FileIn";
            FileIn.Size = new Size(63, 29);
            FileIn.TabIndex = 0;
            FileIn.Text = "File";
            FileIn.UseVisualStyleBackColor = true;
            FileIn.CheckedChanged += FileIn_CheckedChanged;
            // 
            // OutputBox
            // 
            OutputBox.Controls.Add(CopyOut);
            OutputBox.Controls.Add(FileOut);
            OutputBox.Location = new Point(623, 33);
            OutputBox.Name = "OutputBox";
            OutputBox.Size = new Size(300, 164);
            OutputBox.TabIndex = 1;
            OutputBox.TabStop = false;
            OutputBox.Text = "Select output mode";
            // 
            // CopyOut
            // 
            CopyOut.AutoSize = true;
            CopyOut.Checked = true;
            CopyOut.Location = new Point(6, 40);
            CopyOut.Name = "CopyOut";
            CopyOut.Size = new Size(99, 29);
            CopyOut.TabIndex = 1;
            CopyOut.TabStop = true;
            CopyOut.Text = "Text out";
            CopyOut.UseVisualStyleBackColor = true;
            // 
            // FileOut
            // 
            FileOut.AutoSize = true;
            FileOut.Location = new Point(6, 100);
            FileOut.Name = "FileOut";
            FileOut.Size = new Size(63, 29);
            FileOut.TabIndex = 0;
            FileOut.Text = "File";
            FileOut.UseVisualStyleBackColor = true;
            // 
            // SplitMessage
            // 
            SplitMessage.Location = new Point(419, 100);
            SplitMessage.Name = "SplitMessage";
            SplitMessage.Size = new Size(177, 83);
            SplitMessage.TabIndex = 2;
            SplitMessage.Text = "Split Message";
            SplitMessage.UseVisualStyleBackColor = true;
            SplitMessage.Click += SplitMessage_Click;
            // 
            // TextInputBox
            // 
            TextInputBox.Location = new Point(90, 208);
            TextInputBox.Name = "TextInputBox";
            TextInputBox.Size = new Size(381, 412);
            TextInputBox.TabIndex = 3;
            TextInputBox.Text = "";
            // 
            // OutputTextBox
            // 
            OutputTextBox.Location = new Point(537, 208);
            OutputTextBox.Name = "OutputTextBox";
            OutputTextBox.ReadOnly = true;
            OutputTextBox.Size = new Size(386, 412);
            OutputTextBox.TabIndex = 4;
            OutputTextBox.Text = "";
            // 
            // textBox2
            // 
            textBox2.Location = new Point(90, 286);
            textBox2.Name = "textBox2";
            textBox2.ReadOnly = true;
            textBox2.ScrollBars = ScrollBars.Horizontal;
            textBox2.Size = new Size(274, 31);
            textBox2.TabIndex = 6;
            textBox2.Visible = false;
            // 
            // browseInput
            // 
            browseInput.Location = new Point(359, 284);
            browseInput.Name = "browseInput";
            browseInput.Size = new Size(112, 34);
            browseInput.TabIndex = 7;
            browseInput.Text = "browse...";
            browseInput.UseVisualStyleBackColor = true;
            browseInput.Visible = false;
            browseInput.Click += browseInput_Click;
            // 
            // NitroBox
            // 
            NitroBox.Controls.Add(lacksNitroButton);
            NitroBox.Controls.Add(hasNitroButton);
            NitroBox.Location = new Point(409, 22);
            NitroBox.Name = "NitroBox";
            NitroBox.Size = new Size(198, 72);
            NitroBox.TabIndex = 8;
            NitroBox.TabStop = false;
            NitroBox.Text = "Do you have Nitro?";
            // 
            // lacksNitroButton
            // 
            lacksNitroButton.AutoSize = true;
            lacksNitroButton.Checked = true;
            lacksNitroButton.Location = new Point(126, 30);
            lacksNitroButton.Name = "lacksNitroButton";
            lacksNitroButton.Size = new Size(61, 29);
            lacksNitroButton.TabIndex = 1;
            lacksNitroButton.TabStop = true;
            lacksNitroButton.Text = "No";
            lacksNitroButton.UseVisualStyleBackColor = true;
            // 
            // hasNitroButton
            // 
            hasNitroButton.AutoSize = true;
            hasNitroButton.Location = new Point(10, 30);
            hasNitroButton.Name = "hasNitroButton";
            hasNitroButton.Size = new Size(62, 29);
            hasNitroButton.TabIndex = 0;
            hasNitroButton.Text = "Yes";
            hasNitroButton.UseVisualStyleBackColor = true;
            hasNitroButton.CheckedChanged += hasNitroButton_CheckedChanged;
            // 
            // textInputDialogue
            // 
            textInputDialogue.FileName = "openFileDialog1";
            textInputDialogue.Filter = "Text files (*.txt)|*.txt";
            textInputDialogue.Title = "Select message input file";
            // 
            // textOutputDialogue
            // 
            textOutputDialogue.Filter = "Text Files (*.txt)|*.txt|All Files (*.*)|*.*";
            textOutputDialogue.Title = "Choose location of output txt file";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1009, 683);
            Controls.Add(NitroBox);
            Controls.Add(browseInput);
            Controls.Add(textBox2);
            Controls.Add(SplitMessage);
            Controls.Add(OutputBox);
            Controls.Add(InputBox);
            Controls.Add(TextInputBox);
            Controls.Add(OutputTextBox);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            InputBox.ResumeLayout(false);
            InputBox.PerformLayout();
            OutputBox.ResumeLayout(false);
            OutputBox.PerformLayout();
            NitroBox.ResumeLayout(false);
            NitroBox.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private GroupBox InputBox;
        private RadioButton TextIn;
        private RadioButton FileIn;
        private GroupBox OutputBox;
        private RadioButton CopyOut;
        private RadioButton FileOut;
        private Button SplitMessage;
        private RichTextBox TextInputBox;
        private RichTextBox OutputTextBox;
        private TextBox InputFilePath;
        private Button button1;
        private TextBox textBox2;
        private Button browseInput;
        private GroupBox NitroBox;
        private RadioButton lacksNitroButton;
        private RadioButton hasNitroButton;
        private OpenFileDialog textInputDialogue;
        private SaveFileDialog textOutputDialogue;
    }
}
