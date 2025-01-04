using System.CodeDom.Compiler;
using System.ComponentModel.DataAnnotations;

namespace BoardGame
{
    public partial class Form1 : Form
    {
        private Board_Tile[,] tiles = new Board_Tile[13, 13];
        const int length = 13;
        const int width = 13;
        Player player1 = new Player(true);
        Player player2 = new Player(false);
        Color p1c = Color.Green;
        Color p2c = Color.Yellow;
        Color both = Color.RebeccaPurple;
        Random random = new Random();
        private Suspect[] suspects = new Suspect[5];

        Suspect new_sus = new Suspect();


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            populate();
            Suspect.suspect_test(new_sus);
            suspects[0] = new_sus;
            suspects[1] = new_sus;
            suspects[2] = new_sus;
            suspects[3] = new_sus;
            suspects[4] = new_sus;

        }

        private void populate()
        {
            int len = 12;
            int wid = 12;



            for (int y = 0; y < length; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    Board_Tile to_insert = new Board_Tile();
                    to_insert.Size = new Size(100, 100);
                    to_insert.BackColor = Color.White;
                    to_insert.Location = new Point(wid, len);
                    to_insert.MouseClick += Tile_MouseClick;
                    to_insert.tile = new Tile(x, y);
                    tiles[y, x] = to_insert;
                    this.Controls.Add(tiles[y, x]);
                    wid += 106;
                }
                wid = 12;
                len += 106;
            }

            tiles[0, 0].tile.occupied = true;
            tiles[12, 12].tile.occupied = true;

            player1.set_occupied_tile(tiles[0, 0]);
            player2.set_occupied_tile(tiles[12, 12]);

            set_specials();

            player1.set_moves(random.Next(1, 7));
            player2.set_moves(random.Next(1, 7));

         
        

            occupy_tile(tiles[0, 0], p1c);
            occupy_tile(tiles[12, 12], p2c);

            label1.Text = String.Format("Turns: {0}", player1.get_moves());
        }

        private void set_specials()
        {
            for (int y = 5; y <= 7; y++)
            {
                for (int x = 5; x <= 7; x++)
                {
                    tiles[x, y].tile.blocker = true;
                    tiles[x, y].BackColor = Color.IndianRed;
                }
            }

            tiles[4, 6].tile.action_block = true;
            tiles[4, 6].BackColor = Color.LightSteelBlue;
            tiles[6, 4].tile.action_block = true;
            tiles[6, 4].BackColor = Color.LightSteelBlue;
            tiles[8, 6].tile.action_block = true;
            tiles[8, 6].BackColor = Color.LightSteelBlue;
            tiles[6, 8].tile.action_block = true;
            tiles[6, 8].BackColor = Color.LightSteelBlue;

            tiles[1, 5].tile.action_block = true;
            tiles[1, 5].BackColor = Color.Indigo;
            tiles[4, 10].tile.action_block = true;
            tiles[4, 10].BackColor = Color.Cyan;
            tiles[9, 8].tile.action_block = true;
            tiles[9, 8].BackColor = Color.Lime;
            tiles[11, 3].tile.action_block = true;
            tiles[11, 3].BackColor = Color.Maroon;
            tiles[5, 0].tile.action_block = true;
            tiles[5, 0].BackColor = Color.Black;




        }


        private void occupy_tile(Board_Tile b_tile, Color player_col)
        {
            b_tile.BackColor = player_col;


            (int, int) up_coords = b_tile.tile.valid_direction("top");
            (int, int) down_coords = b_tile.tile.valid_direction("bottom");
            (int, int) left_coords = b_tile.tile.valid_direction("left");
            (int, int) right_coords = b_tile.tile.valid_direction("right");

            if (up_coords != (-1, -1))
            {
                color_tile(tiles[up_coords.Item2, up_coords.Item1], Color.DarkCyan);
            }

            if (down_coords != (-1, -1))
            {
                color_tile(tiles[down_coords.Item2, down_coords.Item1], Color.DarkCyan);
            }

            if (left_coords != (-1, -1))
            {
                color_tile(tiles[left_coords.Item2, left_coords.Item1], Color.DarkCyan);
            }

            if (right_coords != (-1, -1))
            {
                color_tile(tiles[right_coords.Item2, right_coords.Item1], Color.DarkCyan);
            }
        }



        private void color_tile(Board_Tile b_tile, Color color)
        {
            {
                if (!b_tile.tile.get_cords().Equals((-1, -1)) && !b_tile.tile.occupied && !b_tile.tile.blocker && !b_tile.tile.action_block)
                {
                    b_tile.BackColor = color;
                }
            }
        }

        private void relinquish_tile(Board_Tile b_tile)
        {
            b_tile.BackColor = Color.White;


            (int, int) up_coords = b_tile.tile.valid_direction("top");
            (int, int) down_coords = b_tile.tile.valid_direction("bottom");
            (int, int) left_coords = b_tile.tile.valid_direction("left");
            (int, int) right_coords = b_tile.tile.valid_direction("right");

            if (up_coords != (-1, -1))
            {
                color_tile(tiles[up_coords.Item2, up_coords.Item1], Color.White);
            }

            if (down_coords != (-1, -1))
            {
                color_tile(tiles[down_coords.Item2, down_coords.Item1], Color.White);
            }

            if (left_coords != (-1, -1))
            {
                color_tile(tiles[left_coords.Item2, left_coords.Item1], Color.White);
            }

            if (right_coords != (-1, -1))
            {
                color_tile(tiles[right_coords.Item2, right_coords.Item1], Color.White);
            }

        }

        private void player_move(Player player, Board_Tile b_tile)
        {
            player.set_moves(player.get_moves() - 1);

            if (b_tile.tile.occupied == true && !b_tile.tile.action_block)
            {
                occupy_tile(b_tile, both);
                relinquish_tile(player.get_occupied_tile());
                player.get_occupied_tile().tile.occupied = false;
                player.set_occupied_tile(b_tile);
                occupy_tile(b_tile, both);
                return;
            }

            if (b_tile.tile.action_block == true)
            {
                Color temp = b_tile.BackColor;
                occupy_tile(b_tile, temp);
                relinquish_tile(player.get_occupied_tile());
                player.get_occupied_tile().tile.occupied = false;
                player.set_occupied_tile(b_tile);
                b_tile.tile.occupied = true;
                occupy_tile(b_tile, temp);

                return;
            }

            relinquish_tile(player.get_occupied_tile());

            player.get_occupied_tile().tile.occupied = false;
            b_tile.tile.occupied = true;

            player.set_occupied_tile(b_tile);


            if (player == player1)
            {
                occupy_tile(b_tile, p1c);
                occupy_tile(player2.get_occupied_tile(), p2c);
                tiles[4, 6].tile.action_block = true;
                tiles[4, 6].BackColor = Color.LightSteelBlue;
                tiles[6, 4].tile.action_block = true;
                tiles[6, 4].BackColor = Color.LightSteelBlue;
                tiles[8, 6].tile.action_block = true;
                tiles[8, 6].BackColor = Color.LightSteelBlue;
                tiles[6, 8].tile.action_block = true;
                tiles[6, 8].BackColor = Color.LightSteelBlue;
                tiles[1, 5].tile.action_block = true;
                tiles[1, 5].BackColor = Color.Indigo;
                tiles[4, 10].tile.action_block = true;
                tiles[4, 10].BackColor = Color.Cyan;
                tiles[9, 8].tile.action_block = true;
                tiles[9, 8].BackColor = Color.Lime;
                tiles[11, 3].tile.action_block = true;
                tiles[11, 3].BackColor = Color.Maroon;
                tiles[5, 0].tile.action_block = true;
                tiles[5, 0].BackColor = Color.Black;
            }

            else
            {
                occupy_tile(b_tile, p2c);
                occupy_tile(player1.get_occupied_tile(), p1c);
                tiles[4, 6].tile.action_block = true;
                tiles[4, 6].BackColor = Color.LightSteelBlue;
                tiles[6, 4].tile.action_block = true;
                tiles[6, 4].BackColor = Color.LightSteelBlue;
                tiles[8, 6].tile.action_block = true;
                tiles[8, 6].BackColor = Color.LightSteelBlue;
                tiles[6, 8].tile.action_block = true;
                tiles[6, 8].BackColor = Color.LightSteelBlue;

                tiles[1, 5].tile.action_block = true;
                tiles[1, 5].BackColor = Color.Indigo;
                tiles[4, 10].tile.action_block = true;
                tiles[4, 10].BackColor = Color.Cyan;
                tiles[9, 8].tile.action_block = true;
                tiles[9, 8].BackColor = Color.Lime;
                tiles[11, 3].tile.action_block = true;
                tiles[11, 3].BackColor = Color.Maroon;
                tiles[5, 0].tile.action_block = true;
                tiles[5, 0].BackColor = Color.Black;

                tiles[4, 6].MouseClick -= Tile_MouseClick;
                tiles[6, 4].MouseClick -= Tile_MouseClick;
                tiles[8, 6].MouseClick -= Tile_MouseClick;
                tiles[6, 8].MouseClick -= Tile_MouseClick;


                tiles[4, 6].MouseClick += Intecept_MouseClick;
                tiles[6, 4].MouseClick += Intecept_MouseClick;
                tiles[8, 6].MouseClick += Intecept_MouseClick;
                tiles[6, 8].MouseClick += Intecept_MouseClick;

                tiles[1, 5].MouseClick -= Tile_MouseClick;
                tiles[4, 10].MouseClick -= Tile_MouseClick;
                tiles[9, 8].MouseClick -= Tile_MouseClick;
                tiles[11, 3].MouseClick -= Tile_MouseClick;
                tiles[5, 0].MouseClick -= Tile_MouseClick;

                tiles[1, 5].MouseClick += Clue_MouseClick;
                tiles[1, 5].clue_num = 1;
                tiles[1, 5].clue = "test1";
                tiles[4, 10].MouseClick += Clue_MouseClick;
                tiles[4, 10].clue_num = 2;
                tiles[4, 10].clue = "test2";
                tiles[9, 8].MouseClick += Clue_MouseClick;
                tiles[9, 8].clue_num = 3;
                tiles[9, 8].clue = "test3";
                tiles[11, 3].MouseClick += Clue_MouseClick;
                tiles[11, 3].clue_num = 4;
                tiles[11, 3].clue = "test 4";
                tiles[5, 0].MouseClick += Clue_MouseClick;
                tiles[5, 0].clue_num = 5;
                tiles[5, 0].clue = "test 5";



            }



        }

        private void Tile_MouseClick(object sender, MouseEventArgs e)
        {
            Board_Tile clickedPanel = sender as Board_Tile;
            if (clickedPanel != null)
            {
                if (player1.get_turn() == true && !player1.waiting)
                {
                    if (player1.get_occupied_tile().tile.neighbours.ContainsValue(clickedPanel.tile.get_cords()) && !clickedPanel.tile.blocker)
                    {

                        player_move(player1, clickedPanel);
                        label1.Text = String.Format("Turns: {0}", player1.get_moves());
                    }

                    if (player1.get_moves() == 0)
                    {
                        player1.set_turn(false);
                        player2.set_turn(true);
                        player2.set_moves(random.Next(1, 7));
                        label1.Text = String.Format("Turns: {0}", player2.get_moves());
                    }
                }


                if (player2.get_turn() == true && !player2.waiting)
                {
                    if (player2.get_occupied_tile().tile.neighbours.ContainsValue(clickedPanel.tile.get_cords()) && !clickedPanel.tile.blocker)
                    {

                        player_move(player2, clickedPanel);
                        label1.Text = String.Format("Turns: {0}", player2.get_moves());
                    }

                    if (player2.get_moves() == 0)
                    {
                        player2.set_turn(false);
                        player1.set_turn(true);
                        player1.set_moves(random.Next(1, 7));
                        label1.Text = String.Format("Turns: {0}", player1.get_moves());
                    }
                }

            }
        }

        private void Intecept_MouseClick(object sender, MouseEventArgs e)
        {
            Board_Tile clickedPanel = sender as Board_Tile;
            if (clickedPanel != null)
            {
                if (player1.get_turn() == true && !player1.waiting)
                {
                    if (player1.get_occupied_tile().tile.neighbours.ContainsValue(clickedPanel.tile.get_cords()) && !clickedPanel.tile.blocker)
                    {

                        player_move(player1, clickedPanel);
                        label1.Text = String.Format("Turns: {0}", player1.get_moves());
                    }

                    if (player1.get_moves() == 0)
                    {
                        Steal form2 = new Steal(player1, player2, random.Next(1, 3));
                        form2.ShowDialog();
                        player1.set_turn(false);
                        player2.set_turn(true);
                        player2.set_moves(random.Next(1, 7));
                        label1.Text = String.Format("Turns: {0}", player2.get_moves());

                    }
                }

                if (player2.get_turn() == true && !player2.waiting)
                {
                    if (player2.get_occupied_tile().tile.neighbours.ContainsValue(clickedPanel.tile.get_cords()) && !clickedPanel.tile.blocker)
                    {

                        player_move(player2, clickedPanel);
                        label1.Text = String.Format("Turns: {0}", player2.get_moves());
                    }

                    if (player2.get_moves() == 0)
                    {
                        Steal form2 = new Steal(player1, player2, random.Next(1, 3));
                        form2.ShowDialog();
                        player2.set_turn(false);
                        player1.set_turn(true);
                        player1.set_moves(random.Next(1, 7));
                        label1.Text = String.Format("Turns: {0}", player1.get_moves());


                    }
                }

            }
        }

        private void Clue_MouseClick(object sender, MouseEventArgs e)
        {
            int roll = online_roll();
            Board_Tile clickedPanel = sender as Board_Tile;
            if (clickedPanel != null)
            {
                if (player1.get_turn() == true && !player1.waiting)
                {
                    if (player1.get_occupied_tile().tile.neighbours.ContainsValue(clickedPanel.tile.get_cords()) && !clickedPanel.tile.blocker)
                    {

                        player_move(player1, clickedPanel);
                        label1.Text = String.Format("Turns: {0}", player1.get_moves());
                    }

                    if (player1.get_moves() == 0)
                    {
                        if (roll==1 && !player1.clues.ContainsKey(clickedPanel.clue_num))
                        {
                            player1.clues.Add(clickedPanel.clue_num, clickedPanel.clue);
                        }

                        player1.set_turn(false);
                        player2.set_turn(true);
                        player2.set_moves(random.Next(1, 7));
                        label1.Text = String.Format("Turns: {0}", player2.get_moves());
                    }
                }


                if (player2.get_turn() == true && !player2.waiting)
                {
                    if (player2.get_occupied_tile().tile.neighbours.ContainsValue(clickedPanel.tile.get_cords()) && !clickedPanel.tile.blocker)
                    {

                        player_move(player2, clickedPanel);
                        label1.Text = String.Format("Turns: {0}", player2.get_moves());
                    }

                    if (player2.get_moves() == 0)
                    {

                        if (roll==1 && !player2.clues.ContainsKey(clickedPanel.clue_num))
                        {
                            player2.clues.Add(clickedPanel.clue_num,clickedPanel.clue);
                        }
                        player2.set_turn(false);
                        player1.set_turn(true);
                        player1.set_moves(random.Next(1, 7));
                        label1.Text = String.Format("Turns: {0}", player1.get_moves());
                    }
                }

            }
        }

        private int online_roll()
        {
            return random.Next(1, 3);
        }
        private void button1_Click(object sender, EventArgs e)
        {
            Evidence form3 = new Evidence(player1);
            form3.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Evidence form3 = new Evidence(player2);
            form3.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form2 form4 = new Form2(suspects);
            form4.Show();
        }
    }
}
