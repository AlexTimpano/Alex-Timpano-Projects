using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BoardGame
{
    public partial class Form2 : Form
    {
        Suspect[] suspects;
        int current = 0;
        internal Form2(Suspect[] suspect)
        {
            InitializeComponent();
            suspects = suspect;
        }

        private void print_clues()
        {
            label1.Text = suspects[current].name;
            textBox1.Text = "";
            for (int i = 0; i < 5; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    textBox1.Text += String.Format("{0}, ", suspects[current].clues[i, j]);
                }
                textBox1.Text += "\r\n\r\n";
            }
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            print_clues();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (current < 4)
            {
                current++;

                print_clues();
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (current > 0)
            {
                current--;
                print_clues();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (suspects[current].guilty == true)
            {
                label2.Text = "Correct! You win";
            }

            else
            {
                label2.Text = "WRONG. You're out!";
            }
        }
    }
}
