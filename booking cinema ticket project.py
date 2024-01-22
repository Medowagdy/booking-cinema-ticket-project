class Movie:
    def __init__(self, title, price, available_tickets):
        self.title = title
        self.price = price
        self.available_tickets = available_tickets

class Client:
    def __init__(self, first_name, last_name, phone_number, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

class Booking:
    def __init__(self, client, movies, payment_method, total_payment, booking_date):
        self.client = client
        self.movies = movies
        self.payment_method = payment_method
        self.total_payment = total_payment
        self.booking_date = booking_date

class CinemaSystem:
    def __init__(self):
        self.movies = []
        self.clients = []
        self.bookings = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def remove_movie(self, movie_title):
        for movie in self.movies:
            if movie.title == movie_title:
                self.movies.remove(movie)
                return

    def set_movie_price(self, movie_title, new_price):
        for movie in self.movies:
            if movie.title == movie_title:
                movie.price = new_price
                return

    def set_movie_available_tickets(self, movie_title, new_available_tickets):
        for movie in self.movies:
            if movie.title == movie_title:
                movie.available_tickets = new_available_tickets
                return

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, client_email):
        for client in self.clients:
            if client.email == client_email:
                self.clients.remove(client)
                return

    def see_transactions(self):
        for booking in self.bookings:
            print(f"Customer name: {booking.client.first_name} {booking.client.last_name}")
            print(f"Booked tickets: {', '.join(movie.title for movie in booking.movies)}")
            print(f"Total payment: {booking.total_payment}")
            print(f"Booking Date: {booking.booking_date}")
            print()

    def add_discount(self, movie_title, discount_percentage):
        for movie in self.movies:
            if movie.title == movie_title:
                movie.price *= (1 - discount_percentage / 100)
                return

    def create_booking(self, client, movies, payment_method, total_payment, booking_date):
        self.bookings.append(Booking(client, movies, payment_method, total_payment, booking_date))