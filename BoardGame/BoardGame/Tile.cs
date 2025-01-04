using System;
using System.Configuration;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;

namespace BoardGame
{
	internal class Tile
	{
		private (int, int) coordinates;
		public Dictionary<string, (int, int)> neighbours = new Dictionary<string, (int, int)>();
		internal bool occupied = false;
		internal bool blocker = false;
		internal bool action_block = false;

		public Tile(int x, int y)
		{ 
			this.coordinates = (x, y);
            create_neighbours();

        }

		private void create_neighbours()
		{
			if (this.coordinates.Item2 > 0)
			{
				this.neighbours["top"]=(this.coordinates.Item1,this.coordinates.Item2-1);
			}

			else
			{
				this.neighbours["top"] = (-1, -1);
			}

			if (this.coordinates.Item2 < 12)
			{
				this.neighbours["bottom"] = (this.coordinates.Item1, this.coordinates.Item2 + 1);
			}

			else
			{
				this.neighbours["bottom"] = (-1, -1);
			}

			if (this.coordinates.Item1 > 0)
			{
				this.neighbours["left"] = (this.coordinates.Item1 - 1, this.coordinates.Item2);
			}

			else
			{
				this.neighbours["left"] = (-1, -1);
			}

			if(this.coordinates.Item1 < 12)
			{
				this.neighbours["right"]= (this.coordinates.Item1 + 1, this.coordinates.Item2);
			}

			else
			{
				this.neighbours["right"] = (-1, -1);
			}
		}

		public (int,int) valid_direction(string direction)
		{
			if (this.neighbours.TryGetValue(direction, out (int,int) value))
			{
				if (this.neighbours[direction].Equals((-1, -1)))
				{
					return (-1,-1);
				}

				else
				{
					return (this.neighbours[direction]);
				}
			}

			else
			{
				return (-1,-1);
			}
		}

		public (int,int) get_cords()
		{
			return this.coordinates;
		}


	}
}
