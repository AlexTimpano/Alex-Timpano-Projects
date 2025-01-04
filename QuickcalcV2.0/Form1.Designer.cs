namespace Quickcalc
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
            this.components = new System.ComponentModel.Container();
            this.inputLabel = new System.Windows.Forms.Label();
            this.outputLabel = new System.Windows.Forms.Label();
            this.arithmeticControls = new System.Windows.Forms.Panel();
            this.inverseButton = new System.Windows.Forms.CheckBox();
            this.shiftButton = new System.Windows.Forms.CheckBox();
            this.tanButton = new System.Windows.Forms.Button();
            this.cosButton = new System.Windows.Forms.Button();
            this.sinButton = new System.Windows.Forms.Button();
            this.piButton = new System.Windows.Forms.Button();
            this.powerButton = new System.Windows.Forms.Button();
            this.closeParen = new System.Windows.Forms.Button();
            this.openParen = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.allClearButton = new System.Windows.Forms.Button();
            this.clearButton = new System.Windows.Forms.Button();
            this.equalButton = new System.Windows.Forms.Button();
            this.divisionButton = new System.Windows.Forms.Button();
            this.multiplicationButton = new System.Windows.Forms.Button();
            this.subtractionButton = new System.Windows.Forms.Button();
            this.additionButton = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.toolTip2 = new System.Windows.Forms.ToolTip(this.components);
            this.button10 = new System.Windows.Forms.Button();
            this.arithmeticControls.SuspendLayout();
            this.SuspendLayout();
            // 
            // inputLabel
            // 
            this.inputLabel.AutoSize = true;
            this.inputLabel.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.inputLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.inputLabel.Location = new System.Drawing.Point(245, 9);
            this.inputLabel.MaximumSize = new System.Drawing.Size(299, 20);
            this.inputLabel.MinimumSize = new System.Drawing.Size(299, 20);
            this.inputLabel.Name = "inputLabel";
            this.inputLabel.Size = new System.Drawing.Size(299, 20);
            this.inputLabel.TabIndex = 1;
            // 
            // outputLabel
            // 
            this.outputLabel.AutoSize = true;
            this.outputLabel.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.outputLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.outputLabel.Location = new System.Drawing.Point(245, 43);
            this.outputLabel.MaximumSize = new System.Drawing.Size(299, 20);
            this.outputLabel.MinimumSize = new System.Drawing.Size(299, 20);
            this.outputLabel.Name = "outputLabel";
            this.outputLabel.Size = new System.Drawing.Size(299, 20);
            this.outputLabel.TabIndex = 2;
            // 
            // arithmeticControls
            // 
            this.arithmeticControls.Controls.Add(this.inverseButton);
            this.arithmeticControls.Controls.Add(this.shiftButton);
            this.arithmeticControls.Controls.Add(this.tanButton);
            this.arithmeticControls.Controls.Add(this.cosButton);
            this.arithmeticControls.Controls.Add(this.sinButton);
            this.arithmeticControls.Controls.Add(this.piButton);
            this.arithmeticControls.Controls.Add(this.powerButton);
            this.arithmeticControls.Controls.Add(this.closeParen);
            this.arithmeticControls.Controls.Add(this.openParen);
            this.arithmeticControls.Controls.Add(this.button0);
            this.arithmeticControls.Controls.Add(this.allClearButton);
            this.arithmeticControls.Controls.Add(this.clearButton);
            this.arithmeticControls.Controls.Add(this.equalButton);
            this.arithmeticControls.Controls.Add(this.divisionButton);
            this.arithmeticControls.Controls.Add(this.multiplicationButton);
            this.arithmeticControls.Controls.Add(this.subtractionButton);
            this.arithmeticControls.Controls.Add(this.additionButton);
            this.arithmeticControls.Controls.Add(this.button9);
            this.arithmeticControls.Controls.Add(this.button8);
            this.arithmeticControls.Controls.Add(this.button7);
            this.arithmeticControls.Controls.Add(this.button6);
            this.arithmeticControls.Controls.Add(this.button5);
            this.arithmeticControls.Controls.Add(this.button4);
            this.arithmeticControls.Controls.Add(this.button3);
            this.arithmeticControls.Controls.Add(this.button2);
            this.arithmeticControls.Controls.Add(this.button1);
            this.arithmeticControls.Location = new System.Drawing.Point(131, 63);
            this.arithmeticControls.Name = "arithmeticControls";
            this.arithmeticControls.Size = new System.Drawing.Size(529, 373);
            this.arithmeticControls.TabIndex = 3;
            // 
            // inverseButton
            // 
            this.inverseButton.AutoSize = true;
            this.inverseButton.Location = new System.Drawing.Point(35, 67);
            this.inverseButton.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.inverseButton.Name = "inverseButton";
            this.inverseButton.Size = new System.Drawing.Size(97, 24);
            this.inverseButton.TabIndex = 25;
            this.inverseButton.Text = "reciprocal";
            this.inverseButton.UseVisualStyleBackColor = true;
            this.inverseButton.CheckedChanged += new System.EventHandler(this.alphaButton_CheckedChanged);
            // 
            // shiftButton
            // 
            this.shiftButton.AutoSize = true;
            this.shiftButton.Location = new System.Drawing.Point(35, 33);
            this.shiftButton.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.shiftButton.Name = "shiftButton";
            this.shiftButton.Size = new System.Drawing.Size(77, 24);
            this.shiftButton.TabIndex = 24;
            this.shiftButton.Text = "inverse";
            this.shiftButton.UseVisualStyleBackColor = true;
            this.shiftButton.CheckedChanged += new System.EventHandler(this.checkBox1_CheckedChanged);
            // 
            // tanButton
            // 
            this.tanButton.Location = new System.Drawing.Point(153, 295);
            this.tanButton.Name = "tanButton";
            this.tanButton.Size = new System.Drawing.Size(50, 51);
            this.tanButton.TabIndex = 23;
            this.tanButton.Text = "tan";
            this.tanButton.UseVisualStyleBackColor = true;
            this.tanButton.Click += new System.EventHandler(this.tan_Click);
            // 
            // cosButton
            // 
            this.cosButton.Location = new System.Drawing.Point(321, 239);
            this.cosButton.Name = "cosButton";
            this.cosButton.Size = new System.Drawing.Size(50, 51);
            this.cosButton.TabIndex = 22;
            this.cosButton.Text = "cos";
            this.cosButton.UseVisualStyleBackColor = true;
            this.cosButton.Click += new System.EventHandler(this.cosButton_Click);
            // 
            // sinButton
            // 
            this.sinButton.Location = new System.Drawing.Point(265, 239);
            this.sinButton.Name = "sinButton";
            this.sinButton.Size = new System.Drawing.Size(50, 51);
            this.sinButton.TabIndex = 21;
            this.sinButton.Text = "sin";
            this.sinButton.UseVisualStyleBackColor = true;
            this.sinButton.Click += new System.EventHandler(this.sinButton_Click);
            // 
            // piButton
            // 
            this.piButton.Location = new System.Drawing.Point(209, 239);
            this.piButton.Name = "piButton";
            this.piButton.Size = new System.Drawing.Size(50, 51);
            this.piButton.TabIndex = 20;
            this.piButton.Text = "π";
            this.piButton.UseVisualStyleBackColor = true;
            this.piButton.Click += new System.EventHandler(this.piButton_Click);
            // 
            // powerButton
            // 
            this.powerButton.Location = new System.Drawing.Point(153, 239);
            this.powerButton.Name = "powerButton";
            this.powerButton.Size = new System.Drawing.Size(50, 51);
            this.powerButton.TabIndex = 19;
            this.powerButton.Text = "x^n";
            this.powerButton.UseVisualStyleBackColor = true;
            this.powerButton.Click += new System.EventHandler(this.powerButton_Click);
            // 
            // closeParen
            // 
            this.closeParen.Location = new System.Drawing.Point(265, 187);
            this.closeParen.Name = "closeParen";
            this.closeParen.Size = new System.Drawing.Size(50, 51);
            this.closeParen.TabIndex = 18;
            this.closeParen.Text = ")";
            this.closeParen.UseVisualStyleBackColor = true;
            this.closeParen.Click += new System.EventHandler(this.closeParen_Click);
            // 
            // openParen
            // 
            this.openParen.Location = new System.Drawing.Point(209, 187);
            this.openParen.Name = "openParen";
            this.openParen.Size = new System.Drawing.Size(50, 51);
            this.openParen.TabIndex = 17;
            this.openParen.Text = "(";
            this.openParen.UseVisualStyleBackColor = true;
            this.openParen.Click += new System.EventHandler(this.openParen_Click);
            // 
            // button0
            // 
            this.button0.Location = new System.Drawing.Point(153, 183);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(50, 51);
            this.button0.TabIndex = 16;
            this.button0.Text = "0";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // allClearButton
            // 
            this.allClearButton.BackColor = System.Drawing.Color.Coral;
            this.allClearButton.Location = new System.Drawing.Point(265, 295);
            this.allClearButton.Name = "allClearButton";
            this.allClearButton.Size = new System.Drawing.Size(50, 51);
            this.allClearButton.TabIndex = 15;
            this.allClearButton.Text = "AC";
            this.allClearButton.UseVisualStyleBackColor = false;
            this.allClearButton.Click += new System.EventHandler(this.allClearButton_Click);
            // 
            // clearButton
            // 
            this.clearButton.BackColor = System.Drawing.Color.Coral;
            this.clearButton.Location = new System.Drawing.Point(209, 295);
            this.clearButton.Name = "clearButton";
            this.clearButton.Size = new System.Drawing.Size(50, 51);
            this.clearButton.TabIndex = 14;
            this.clearButton.Text = "C";
            this.clearButton.UseVisualStyleBackColor = false;
            this.clearButton.Click += new System.EventHandler(this.clearButton_Click);
            // 
            // equalButton
            // 
            this.equalButton.BackColor = System.Drawing.SystemColors.Highlight;
            this.equalButton.Location = new System.Drawing.Point(321, 295);
            this.equalButton.Name = "equalButton";
            this.equalButton.Size = new System.Drawing.Size(50, 51);
            this.equalButton.TabIndex = 13;
            this.equalButton.Text = "=";
            this.equalButton.UseVisualStyleBackColor = false;
            this.equalButton.Click += new System.EventHandler(this.equalButton_Click);
            // 
            // divisionButton
            // 
            this.divisionButton.Location = new System.Drawing.Point(321, 187);
            this.divisionButton.Name = "divisionButton";
            this.divisionButton.Size = new System.Drawing.Size(50, 51);
            this.divisionButton.TabIndex = 12;
            this.divisionButton.Text = "÷";
            this.divisionButton.UseVisualStyleBackColor = true;
            this.divisionButton.Click += new System.EventHandler(this.divisionButton_Click);
            // 
            // multiplicationButton
            // 
            this.multiplicationButton.Location = new System.Drawing.Point(321, 131);
            this.multiplicationButton.Name = "multiplicationButton";
            this.multiplicationButton.Size = new System.Drawing.Size(50, 51);
            this.multiplicationButton.TabIndex = 11;
            this.multiplicationButton.Text = "×";
            this.multiplicationButton.UseVisualStyleBackColor = true;
            this.multiplicationButton.Click += new System.EventHandler(this.multiplicationButton_Click);
            // 
            // subtractionButton
            // 
            this.subtractionButton.Location = new System.Drawing.Point(321, 75);
            this.subtractionButton.Name = "subtractionButton";
            this.subtractionButton.Size = new System.Drawing.Size(50, 51);
            this.subtractionButton.TabIndex = 10;
            this.subtractionButton.Text = "-";
            this.subtractionButton.UseVisualStyleBackColor = true;
            this.subtractionButton.Click += new System.EventHandler(this.subtractionButton_Click);
            // 
            // additionButton
            // 
            this.additionButton.Location = new System.Drawing.Point(321, 19);
            this.additionButton.Name = "additionButton";
            this.additionButton.Size = new System.Drawing.Size(50, 51);
            this.additionButton.TabIndex = 9;
            this.additionButton.Text = "+";
            this.additionButton.UseVisualStyleBackColor = true;
            this.additionButton.Click += new System.EventHandler(this.additionButton_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(265, 131);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(50, 51);
            this.button9.TabIndex = 8;
            this.button9.Text = "9";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(209, 131);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(50, 51);
            this.button8.TabIndex = 7;
            this.button8.Text = "8";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(153, 131);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(50, 51);
            this.button7.TabIndex = 6;
            this.button7.Text = "7";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(265, 75);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(50, 51);
            this.button6.TabIndex = 5;
            this.button6.Text = "6";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(209, 75);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(50, 51);
            this.button5.TabIndex = 4;
            this.button5.Text = "5";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(153, 75);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(50, 51);
            this.button4.TabIndex = 3;
            this.button4.Text = "4";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(265, 19);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(50, 51);
            this.button3.TabIndex = 2;
            this.button3.Text = "3";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(209, 19);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(50, 51);
            this.button2.TabIndex = 1;
            this.button2.Text = "2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(153, 19);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(50, 51);
            this.button1.TabIndex = 0;
            this.button1.Text = "1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(28, 214);
            this.button10.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(86, 31);
            this.button10.TabIndex = 4;
            this.button10.Text = "Graphing";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 451);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.arithmeticControls);
            this.Controls.Add(this.outputLabel);
            this.Controls.Add(this.inputLabel);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.arithmeticControls.ResumeLayout(false);
            this.arithmeticControls.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Label inputLabel;
        private Label outputLabel;
        private Panel arithmeticControls;
        private Button button6;
        private Button button5;
        private Button button4;
        private Button button3;
        private Button button2;
        private Button button1;
        private ToolTip toolTip1;
        private Button allClearButton;
        private Button clearButton;
        private Button equalButton;
        private Button divisionButton;
        private Button multiplicationButton;
        private Button subtractionButton;
        private Button additionButton;
        private Button button9;
        private Button button8;
        private Button button7;
        private Button button0;
        private Button closeParen;
        private Button openParen;
        private Button powerButton;
        private Button piButton;
        private Button sinButton;
        private Button tanButton;
        private Button cosButton;
        private ToolTip toolTip2;
        private CheckBox shiftButton;
        private CheckBox inverseButton;
        private Button button10;
    }
}