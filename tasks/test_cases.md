# Задача 1.
Input:
```
3
LEarn Python, The site contains content about python programming language
learn python, New description
Learn C++, c++ site description.
```
Output:
```
{'Learn Python'} = 2.
```

Input:
```
4
google, An American multinational corporation.
Google, The most popular search engine in the world.
Microsoft, one of the largest multinational companies producing proprietary software for various types of computing equipment
microsoft, the company that developed the worst operating system.
```

Output:
```
{'google'} = 2
{'microsoft'} = 2
```

Input: 
```
10
gOogle, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
microsoft, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
Microsoft, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
AMD, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
Ubuntu, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
Google, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
Bubuntu, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
google, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
ubuntu, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
bing, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt et augue id tempor. Ut.
```

Output: 

```
{'google'} = 3
{'microsoft'} = 2
{'ubuntu'} = 2
```

# Задача 2.

Input:
```
7
Andrew Walker -> Max Smith
Sara Stewart -> Kenneth Jones
William Mills -> Kenneth Jones
Joseph Ross -> Max Smith
Elsie Chapman -> William Johnson
Elsie Chapman -> Max Smith
Elsie Chapman -> Kenneth Jones
Elsie Chapman
```
Output:
```
Elsie Chapman: 600₽
```

Input:
```
100
Janice Hall -> Joshua Roberts
Marshall Wells -> Mary Munoz
Michael Reeves -> Holly May
Gordon Stewart -> Rose Kim
Donald Perkins -> Esther Oliver
Donna Rogers -> Nancy Smith
Maureen Williams -> Katie Graham
Richard Medina -> Maria Ramirez
Rosa Wright -> William Smith
Donald Anderson -> Ashley Davis
Benjamin Silva -> James McDonald
Bertha Jenkins -> Sandra Richardson
Thomas Simpson -> Kristen Franklin
Susan Wood -> David Nelson
Annette Stevens -> Michael Boyd
Curtis Norman -> David Fuller
Wanda Griffin -> Amy Alvarez
Douglas Jackson -> Erik Robinson
Ellen Quinn -> Barbara Lopez
Joshua Lopez -> Renee Thomas
Robert Miles -> Gladys Diaz
Barry Smith -> Stacy Hogan
Heather Jones -> Richard Higgins
Deborah Rice -> Leonard Reynolds
Bob Garza -> Peggy Young
Nancy Lopez -> Terri Bryant
Ricardo Smith -> Gladys Hampton
Peter Barnes -> Kathleen Kelly
Clara Smith -> Martha Washington
Emily Brewer -> Patricia Wilson
Valerie Duncan -> Richard Lee
Andrea Anderson -> Brenda Anderson
Mary Cunningham -> Carla Jackson
Jeremy Burns -> Gary Taylor
Thomas Perkins -> Elizabeth Marsh
Dustin Edwards -> Ashley Phillips
Dorothy Jennings -> Shawn Garcia
Kelly Nichols -> Juanita Davis
Salvador Quinn -> Karen James
Maria Todd -> Julia Morales
Maria Ferguson -> Patrick Johnson
Jennifer Francis -> Julia Baker
Stacy Flores -> Darrell Taylor
Mary Jones -> Rose Graham
Mary Fleming -> David Miller
Crystal Castro -> William Holloway
John Scott -> Christopher Green
Betty Reynolds -> Scott Mendez
Megan Johnson -> Kurt Spencer
Elizabeth Mills -> Betty Rodriguez
Christian Smith -> Carrie Kennedy
Alice Padilla -> Bryan Stone
William Johnson -> Robert Erickson
George Beck -> Timothy Dixon
Geraldine Foster -> Minnie Johnson
Tammy Burton -> Mary Thompson
Tina Webb -> Jill Holloway
Christopher Kelly -> Judith Anderson
Rafael Collins -> Marlene Johnson
Lillie Wright -> Susan Anderson
Colleen Davis -> Kim Martin
Grace Evans -> Justin Hunter
Geraldine Watkins -> Chad Campbell
Cathy Austin -> Cynthia Yates
Shirley Sanders -> Tammy Jones
James Perez -> Kimberly Ford
Debbie Berry -> Julie Taylor
Ronald West -> Julia Parsons
Vivian McLaughlin -> Don Reid
Norma Doyle -> Marion Williams
Carol Peters -> Patricia Burke
Myrtle Brown -> Elsie Wheeler
Shawn Woods -> Patricia Reed
David Armstrong -> Tina Anderson
Gregory Allen -> Earl Hansen
Betty Warren -> Nicole Alexander
Jennifer Jones -> Ana Armstrong
Leo Moody -> John Chambers
Nicole Newman -> James Bates
Diane White -> Michael Austin
Cathy Austin -> Donald Martinez
Kenneth Gill -> Frank Riley
Jeffrey James -> Marie Harris
Judy Walters -> Julia Richards
Regina Rogers -> Chris Cole
Cathy Austin -> Thomas Taylor
Henry Morris -> Anna Scott
Grace Gibson -> Steve Edwards
Terri Banks -> Deborah Allen
Juanita Allen -> Enrique Young
Glenn Simmons -> John Torres
Carol Jones -> Karen Brown
Cathy Austin -> Evelyn Wright
Willie Marsh -> Jill Dunn
Kenneth Moore -> Arthur Robinson
Jerome Martin -> Ralph Murphy
Timothy Alexander -> Debbie Riley
William Jones -> Stanley Smith
Pauline Payne -> Mary Coleman
Ann Davis -> George Hughes
Cathy Austin
```

Output:
```
    Cathy Austin: 800₽
```

# Задача 3.

Input:
```
8
Andrew Walker: 3
Sara Stewart: 5
William Mills: 4
Joseph Ross: 2
Sara Stewart: 5
Joseph Ross: 3
Andrew Walker: 5
William Mills: 4
```
Output:
```
Худший - Joseph Ross
Лучший - Sara Stewart
```

Input:
```
100
David Guerrero: 3
Michael Morris: 3
James Scott: 5
Richard Gilbert: 3
Mary Thomas: 4
Jeremy White: 3
Melissa Underwood: 5
Rose Love: 4
Carlos Pena: 3
Edward White: 3
Julia Jones: 3
Maria Meyer: 4
Benjamin Evans: 5
Lawrence Smith: 5
Martha Lawson: 3
Jacob Santiago: 3
Henry Ball: 4
Jason Brown: 4
Mike Chambers: 3
Arlene Rhodes: 3
Laura Allen: 3
Frances McKinney: 5
Ralph Lawrence: 3
Richard Porter: 3
Lillian Smith: 3
Pauline Miller: 4
Grace Wilson: 3
Wallace Gordon: 4
Crystal Kelly: 3
Sandra Long: 3
Mildred Wheeler: 5
Michael Medina: 5
Patsy Warner: 3
James Padilla: 4
Danielle Luna: 3
Elaine Armstrong: 4
Donna Peterson: 3
Rebecca Young: 4
David Brown: 3
Mary Adams: 3
William Blake: 3
Walter Harrington: 3
Vicki Townsend: 4
Amanda Payne: 4
Judy Taylor: 3
Erica Garcia: 4
Rhonda Farmer: 5
Debra Hicks: 4
Anna Miller: 3
Robert Johnson: 3
Connie Martin: 5
Angela Smith: 3
Charlotte Johnson: 3
Maurice Jackson: 3
Terri Aguilar: 4
Stephanie Thomas: 4
Larry Green: 5
Jessica McDonald: 5
Laura Johnson: 5
Constance Gray: 5
Yolanda Love: 3
Tom Martin: 4
Joseph Ferguson: 4
Pauline Rodriguez: 4
Michael Hardy: 3
Steven Nash: 4
Stephen Gilbert: 4
Kelly Hodges: 5
Sandra Cruz: 5
Carl Williams: 3
David Young: 5
Sheila Tyler: 5
Grace Johnson: 3
Martin Fletcher: 5
Yolanda Love: 2
Tracy Smith: 3
Christina Buchanan: 5
Mary Robinson: 3
Hilda Stewart: 5
Yolanda Love: 3
Michelle Hernandez: 4
Betty Taylor: 3
Aaron Williams: 4
John Lawrence: 3
Janet Webb: 4
Leon Green: 3
Jessica McDonald: 5
Yolanda Love: 2
Ryan Watts: 5
Ernest Turner: 4
Shawn Wright: 3
Mary Smith: 4
Jessica McDonald: 4
Leroy Owens: 5
Christopher McDonald: 3
Jessica McDonald: 5
Jessica McDonald: 5
Salvador Davis: 3
William Clark: 3
Brian Barber: 3
```

Output: 
```
Худший - Yolanda Love
Лучший - James Scott
```

# Задача 4.

Input:
```
{"input_expression":5,"output_expression":120}
```
Output:
```
{'input_expression': '5'}
{'output_expression': '120}'}
```

Input:
```
{"input_expression":6,"output_expression":720,"compile_flags":-wall}
```

Output:
```
{'input_expression': '6'}
{'output_expression': '720'}
{'compile_flags': '-wall'}
```