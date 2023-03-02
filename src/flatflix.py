class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def get_title(self):
        return self.title

    def get_reviews(self):
        return self.reviews

    def get_viewers(self):
        result = []
        for review in self.reviews:
            result.append(review.viewer)
        return result

    def average_rating(self):
        total = 0
        for review in self.reviews:
            total += review.rating
        return total/len(self.reviews)

    def highest_review(self):
        highest = self.reviews[0]
        for review in self.reviews:
            if review.rating > highest.rating:
                highest = review
        return highest



class Viewer:
    def __init__(self, username):
        self.username = username
        self.reviews = []

    def get_username(self):
        return self.username

    def get_reviews(self):
        return self.reviews

    def get_movies(self):
        result = []
        for review in self.reviews:
            result.append(review.movie)
        return result

    def has_reviewed(self, movie):
        for review in self.reviews:
            if(review.movie == movie):
                return True
            else:
                return False

    def rate_movie(self, movie, rating):
        new_review = Review(self, movie, rating)
        self.reviews.append(new_review)


class Review:
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

    def get_rating(self):
        return self.rating

    def get_viewer(self):
        return self.viewer

    def get_movie(self):
        return self.movie
