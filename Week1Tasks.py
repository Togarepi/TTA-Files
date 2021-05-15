{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.4"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python394jvsc74a57bd02fe19c50a04275f338573003ae50a49ea7cd1af55cf624f6f938d5e479942dad",
   "display_name": "Python 3.9.4 64-bit"
  },
  "metadata": {
   "interpreter": {
    "hash": "2fe19c50a04275f338573003ae50a49ea7cd1af55cf624f6f938d5e479942dad"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "# Import random number\n",
    "\n",
    "import random \n",
    "r =random.randint(1,10)\n",
    "print(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "My name is name\n"
     ]
    }
   ],
   "source": [
    "# What is your name\n",
    "\n",
    "def personal_details():\n",
    "    name = input(\"What is your name? \")\n",
    "print(\"My name is name\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-968579fb7691>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mr\u001b[0m \u001b[1;33m=\u001b[0m\u001b[0mrandom\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrandint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mguess\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Guess a number between 1 and 100: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[0mguess\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mnumber\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mguess\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mnumber\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m    846\u001b[0m                 \u001b[1;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    847\u001b[0m             )\n\u001b[1;32m--> 848\u001b[1;33m         return self._input_request(str(prompt),\n\u001b[0m\u001b[0;32m    849\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    850\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m    890\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    891\u001b[0m                 \u001b[1;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 892\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Interrupted by user\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    893\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    894\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Invalid Message:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "# Guess random Number\n",
    "\n",
    "r =random.randint(1,10)\n",
    "guess = int(input(\"Guess a number between 1 and 100: \"))\n",
    "while guess != number:\n",
    "    if guess < number: \n",
    "        print(\"Incorrect try again higher\")\n",
    "        guess = int(input(\"\\nGuess a number between 1 and 100: \"))\n",
    "    else:\n",
    "        print(\"Try again it is lower\")\n",
    "        guess = int(input(\"\\nGuess a number between 1 and 100: \"))\n",
    "\n",
    "print (\"Correct\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "32 Tottenham Hotspurs are a top European football team\n32 Why is Mourinho like a bad carpenter? He is a sore loser\n32 How do you follow Will Smith in the snow? Follow the fresh prints\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "i =random.randint(1,100) \n",
    "my_favourite_num = i\n",
    "i = 32\n",
    "print(str(i) + ( \" Tottenham Hotspurs are a top European football team\"))\n",
    "print(str(i) + ( \" Why is Mourinho like a bad carpenter? He is a sore loser\"))\n",
    "print(str(i) + ( \" How do you follow Will Smith in the snow? Follow the fresh prints\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Your favorite meal is..... with a glass of.....  \n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "metadata": {},
     "execution_count": 3
    }
   ],
   "source": [
    "# Program that asks favorite food and drink\n",
    "\n",
    "first = input(\"Hello, what's your favourite starter? \")\n",
    "second = input(\"Now, now what is your favourite meal and desert and drink? \")\n",
    "print(\"Your favorite meal is..... with a glass of..... \", first + second)\n",
    "\n",
    "input(\"\\n\\nPress the enter key to exit.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Basic Calculator\n",
    "\n",
    "number1 = int(input(\"Enter First Number: \"))\n",
    "number2 = int(input(\"Enter Second Number: \"))\n",
    "\n",
    "print(\"Enter which operation would you like to perform?\")\n",
    "ch = input(\"Enter any of these char for specific operation +,-,*,**,/: \")\n",
    "\n",
    "result = 0\n",
    "if ch == '+':\n",
    "    result = number1 + number2\n",
    "elif ch == '-':\n",
    "    result = number1 - number2\n",
    "elif ch == '*':\n",
    "    result = number1 * number2\n",
    "elif ch == '**':\n",
    "    result = number1 ** number2\n",
    "elif ch = '/':\n",
    "    result = number1 / number2\n",
    "else:\n",
    "    print(\"Input character is not recognised.\")\n",
    "\n",
    "print(number1, ch , number2, \":\", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Simple calculator operation selected\n",
    "\n",
    "number1 = 8\n",
    "number2 = 6\n",
    "ch == input(\"-\")\n",
    "result = 0\n",
    "if ch == \"-\"\n",
    "    print(number1 - number2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-9-1ccc7a166a2d>, line 3)",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-9-1ccc7a166a2d>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    while (x*y < 1000) :\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "for x in range(2000) :\n",
    "    y = (10/100)\n",
    "    while (x*y < 1000) :\n",
    "        if (x = 0): break\n",
    "        print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}