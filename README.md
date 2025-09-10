# Cinema Management System (Python)

## Description
This is a simple Python console application for cinema ticketing and schedule management. 
It includes two roles: Cashier and Customer. Users can browse films, view schedules, add projections, and buy tickets. The application uses text files to store data.

## Features
- Two roles: Cashier and Customer
- Browse all films
- View repertoire
- Add new projections (Cashier)
- Change projection time (Cashier)
- Buy tickets (Customer)
- Track sold tickets
- Simple bar chart visualization of tickets sold per film using matplotlib

## Technologies
- Python 3.x
- matplotlib (for plotting sold tickets)

## File Structure

```
bioskop/
├─ Projekat.py          # main script
├─ Blagajnik.py
├─ Filmovi.py
├─ Karte.py
├─ Repertoar.py
├─ fajlovi/            # contains sample data files
│   ├─ blagajnik.txt
│   ├─ filmovi.txt
│   ├─ prodateKarte.txt
│   └─ repertoar.txt
└─ .gitignore
```

## Requirements
- Python 3.x
- Install matplotlib: `pip install matplotlib`

## How to Run

1. Clone the repository:

```
git clone https://github.com/nadjabozic/cinema-python.git
```

2. Navigate to project folder:

```
cd cinema-python
```

3. Run the main script:

```
python Projekat.py
```

4. Follow the console menu prompts for Cashier or Customer.
