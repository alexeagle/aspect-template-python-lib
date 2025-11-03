import cowsay
from os import path, getenv, sep

# Note, we could use https://pypi.org/project/bazel-runfiles/
# for a more robust lookup mechanism of files provided in the `data` attribute.
WORKSPACE=getenv('BAZEL_WORKSPACE', '')
FOLDER=path.dirname(__file__).split(WORKSPACE + sep)[-1]

MARVIN="""
      \  |
       \ |
        \|
           ---------------
        =--=+++***++++++==---       --
       =-=+##***************=--   =----
      ===+##**=+*******+++***+--+=---==
     ===+##*+:::-*****+-::-***+-==--===
     ===*###**=+*++++++=--+**#*=-+====
   =====*#####***+---+*****###*======
 --=++===**###################*===
---==+++++++++==+++++******++=====
 ====+++*+==+*+===================
   ===++******==================+
       +++++++++=============++=
         +++++++++++++++++++++
           ##%%#+++++#####
            ##%      %%##
"""


def say(text):
    cowsay.draw(text, MARVIN)

def say_stamped(text):
    with open(path.join(FOLDER, "header.txt"), "r") as header:
        cowsay.draw(header.read() + text, MARVIN)
