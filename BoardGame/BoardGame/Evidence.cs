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
    public partial class Evidence : Form
    {
        Player player;
        internal Evidence(Player player)
        {
            InitializeComponent();
            this.player = player;   
        }

        private void Evidence_Load(object sender, EventArgs e)
        {
            foreach(KeyValuePair<int,string> kvp in player.clues)
            {
                textBox1.Text += String.Format("#{0}, {1}\r\n", kvp.Key, kvp.Value);
            }
        }
    }
}
