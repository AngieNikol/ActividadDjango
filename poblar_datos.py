from biblioteca.models import Author, Book, Review

#Author.objects.all().delete()
#Book.objects.all().delete()
#Review.objects.all().delete()

author1, _ = Author.objects.get_or_create(name="Gabriel Garcia Marquez", nationality="Colombiana")
author2, _ = Author.objects.get_or_create(name="Isabel Allende", nationality="Chilena")

book1, _ = Book.objects.get_or_create(title="Cien Anios de Soledad", author=author1, published_date="1967-05-30", abstract="Una novela que narra la historia de la familia Buendía en el pueblo ficticio de Macondo.")
book2, _ = Book.objects.get_or_create(title="La Casa de los Espiritus", author=author2, published_date="1982-01-01", abstract="Una saga familiar que mezcla lo real con lo sobrenatural en el contexto de la historia de Chile.")

review1, _ = Review.objects.get_or_create(book=book1, text="Una obra maestra de la literatura latinoamericana.", rating=5)
review2, _ = Review.objects.get_or_create(book=book2, text="Una novela fascinante que combina historia y magia.", rating=4)

print("Datos de prueba poblados exitosamente.")