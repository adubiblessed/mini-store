from django.db import models

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart - {self.product.name}"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ['added_at']