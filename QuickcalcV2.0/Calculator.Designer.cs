namespace Quickcalc
{
    partial class Calculator
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.leftInterval = new System.Windows.Forms.TextBox();
            this.rightInterval = new System.Windows.Forms.TextBox();
            this.stepBox = new System.Windows.Forms.TextBox();
            this.graphButton = new System.Windows.Forms.Button();
            this.left = new System.Windows.Forms.Label();
            this.right = new System.Windows.Forms.Label();
            this.step = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.errorBox = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // leftInterval
            // 
            this.leftInterval.Location = new System.Drawing.Point(148, 411);
            this.leftInterval.Name = "leftInterval";
            this.leftInterval.Size = new System.Drawing.Size(125, 27);
            this.leftInterval.TabIndex = 0;
            this.leftInterval.Text = "0";
            this.leftInterval.TextChanged += new System.EventHandler(this.leftInterval_TextChanged);
            this.leftInterval.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.leftInterval_KeyPress);
            // 
            // rightInterval
            // 
            this.rightInterval.Location = new System.Drawing.Point(327, 411);
            this.rightInterval.Name = "rightInterval";
            this.rightInterval.Size = new System.Drawing.Size(125, 27);
            this.rightInterval.TabIndex = 1;
            this.rightInterval.Text = "10";
            this.rightInterval.TextChanged += new System.EventHandler(this.rightInterval_TextChanged);
            this.rightInterval.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.rightInterval_KeyPress);
            // 
            // stepBox
            // 
            this.stepBox.Location = new System.Drawing.Point(516, 411);
            this.stepBox.Name = "stepBox";
            this.stepBox.Size = new System.Drawing.Size(125, 27);
            this.stepBox.TabIndex = 2;
            this.stepBox.Text = "1";
            this.stepBox.TextChanged += new System.EventHandler(this.stepBox_TextChanged);
            this.stepBox.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.stepBox_KeyPress);
            // 
            // graphButton
            // 
            this.graphButton.Location = new System.Drawing.Point(547, 12);
            this.graphButton.Name = "graphButton";
            this.graphButton.Size = new System.Drawing.Size(94, 29);
            this.graphButton.TabIndex = 3;
            this.graphButton.Text = "Graph";
            this.graphButton.UseVisualStyleBackColor = true;
            this.graphButton.Click += new System.EventHandler(this.graphButton_Click);
            // 
            // left
            // 
            this.left.AutoSize = true;
            this.left.Location = new System.Drawing.Point(190, 388);
            this.left.Name = "left";
            this.left.Size = new System.Drawing.Size(34, 20);
            this.left.TabIndex = 4;
            this.left.Text = "Left";
            // 
            // right
            // 
            this.right.AutoSize = true;
            this.right.Location = new System.Drawing.Point(367, 388);
            this.right.Name = "right";
            this.right.Size = new System.Drawing.Size(44, 20);
            this.right.TabIndex = 5;
            this.right.Text = "Right";
            // 
            // step
            // 
            this.step.AutoSize = true;
            this.step.Location = new System.Drawing.Point(562, 388);
            this.step.Name = "step";
            this.step.Size = new System.Drawing.Size(39, 20);
            this.step.TabIndex = 6;
            this.step.Text = "Step";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(285, 13);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(218, 27);
            this.textBox1.TabIndex = 7;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(367, 43);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(68, 20);
            this.label1.TabIndex = 8;
            this.label1.Text = "Equation";
            // 
            // errorBox
            // 
            this.errorBox.ForeColor = System.Drawing.Color.Red;
            this.errorBox.Location = new System.Drawing.Point(12, 2);
            this.errorBox.Multiline = true;
            this.errorBox.Name = "errorBox";
            this.errorBox.Size = new System.Drawing.Size(228, 49);
            this.errorBox.TabIndex = 9;
            this.errorBox.Visible = false;
            // 
            // Calculator
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.errorBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.step);
            this.Controls.Add(this.right);
            this.Controls.Add(this.left);
            this.Controls.Add(this.graphButton);
            this.Controls.Add(this.stepBox);
            this.Controls.Add(this.rightInterval);
            this.Controls.Add(this.leftInterval);
            this.Name = "Calculator";
            this.Text = "Calculator";
            this.Load += new System.EventHandler(this.Calculator_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private OxyPlot.WindowsForms.PlotView plotView1;
        private TextBox leftInterval;
        private TextBox rightInterval;
        private TextBox stepBox;
        private Button graphButton;
        private Label left;
        private Label right;
        private Label step;
        private TextBox textBox1;
        private Label label1;
        private TextBox errorBox;
    }
}