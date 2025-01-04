using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BoardGame
{
    public partial class Steal : Form
    {
        Player user;
        Player target;
        int mode;
        internal Steal(Player player1, Player player2, int mode)
        {
            InitializeComponent();
            this.user= player1;
            this.target= player2;
            this.mode = mode;

            this.button1.Hide();
            this.button2.Hide();
            this.button3.Hide();
            this.button4.Hide();
            this.button5.Hide();

        }

        private void Steal_Load(object sender, EventArgs e)
        {
            if (target.clues.Count == 0)
            {
                this.Close();
            }
            if (mode == 1)
            {
                checkBox1.Checked = true;
                checkBox2.Checked = false;
            }

            else
            {
                checkBox1.Checked = false;
                checkBox2.Checked = true;
            }

            for (int i = 1; i <= 5; i++)
            {
                if (mode == 1)
                {
                    if ((target.clues.ContainsKey(i) && !user.clues.ContainsKey(i)))
                    {

                        switch (i)
                        {
                            case 1:
                                button1.Show();
                                break;
                            case 2:
                                button2.Show();
                                break;
                            case 3:
                                button3.Show();
                                break;
                            case 4:
                                button4.Show();
                                break;
                            case 5:
                                button5.Show();
                                break;

                        }
                    }
                }

                else
                {
                    if ((!target.clues.ContainsKey(i) && user.clues.ContainsKey(i)))
                    {

                        switch (i)
                        {
                            case 1:
                                button1.Show();
                                break;
                            case 2:
                                button2.Show();
                                break;
                            case 3:
                                button3.Show();
                                break;
                            case 4:
                                button4.Show();
                                break;
                            case 5:
                                button5.Show();
                                break;

                        }
                    }
                }
            }

            //If all buttons are hidden, nothing to send or steal

            if(Controls.OfType<Button>().All(btn => !btn.Visible)){
                this.Close();
            }

        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (mode == 1)
            {

                string copy = target.clues[1];

                user.clues[1] = copy;
            }

            else
            {
                string copy = user.clues[1];
                target.clues[1] = copy;
            }

            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (mode == 1)
            {
                string copy = target.clues[2];
                user.clues[2] = copy;
            }
            else
            {
                string copy = user.clues[2];
                target.clues[2] = copy;
            }
            this.Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (mode == 1)
            {
                string copy = target.clues[3];
                user.clues[3] = copy;
            }
            else
            {
                string copy = user.clues[3];
                target.clues[3] = copy;
            }
            this.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (mode == 1)
            {
                string copy = target.clues[4];
                user.clues[4] = copy;
            }
            else
            {
                string copy = user.clues[4];
                target.clues[4] = copy;
            }
            this.Close();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (mode == 1)
            {
                string copy = target.clues[5];
                user.clues[5] = copy;
            }
            else
            {
                string copy = user.clues[5];
                target.clues[5] = copy;
            }
            this.Close();
        }

    }
}
