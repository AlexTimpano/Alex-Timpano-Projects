using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BoardGame
{
    internal class Player
    {
        bool turn;
        int movements;
        public bool waiting = false;
        private Board_Tile occupied_tile;
        internal Dictionary<int, String> clues = new Dictionary<int, String>();    

        public Player(bool turn)
        { 
            this.turn= turn;
        }

        public bool get_turn()
        {
            return this.turn;
        }

        public void set_turn(bool new_turn)
        {
            this.turn=new_turn;
        }

        public int get_moves()
        {
            return this.movements;
        }

        public void set_moves(int new_moves)
        {
            this.movements = new_moves;
        }

        public Board_Tile get_occupied_tile()
        {
            return occupied_tile;
        }

        public void set_occupied_tile(Board_Tile new_occupied_tile)
        {
            this.occupied_tile=new_occupied_tile;   
        }

        public static void test_clues(Player player1, Player player2)
        {
            player1.clues[1] = "Smokes";
            player1.clues[2] = "Drinks";
            player1.clues[3] = "Sleeps";

            player2.clues[4] = "Reads";
            player2.clues[5] = "Studiees";
        }
   
    }
}
