using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using System.Text;
using System.Threading.Tasks;

namespace BoardGame
{
    internal class Suspect
    {
        internal bool guilty;
        internal string name="";
        internal string[,] clues = new string[5, 4];


        public Suspect()
        {

        }

        public static void suspect_test(Suspect suspect)
        {
            suspect.guilty = true;
            suspect.name = "William Smith";
            string[,] source_clues = new string[5, 4]
            {
                {"Bloodstains","Poisonous substances","Missing weapon","Lights off" },
                {"Was overheard planning it","Bystander claims to have witnessed it","Security footage shows them in the act","Friend gives character witness" },
                {"DNA evidence points to suspect","IP address points to their location","Purchased suspicious materials","Fingerprints found at crime scene"  },
                {"Intercepted communications discussing crime","Suspect met with shady people","Suspicious money transfers after crime","Uses Twitter" },
                {"Suspect lacks alibi","Suspect got nervous","Friends pointed them out for the crime","Suspect confessed" }
            };

            for (int i = 0; i < source_clues.GetLength(0); i++)
            {
                for (int j = 0; j < source_clues.GetLength(1); j++)
                {
                    suspect.clues[i, j] = source_clues[i, j];
                }
            }
        }
    }

   
}
