"""
Serializers for recipe APIs
"""

from rest_framework import serializers
from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe object"""
    # ingredients = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Ingredient.objects.all(),
    # )
    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all(),
    # )

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes',
            'price', 'link',
        ]
        read_only_fields = ['id',]

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail object"""
    # ingredients = IngredientSerializer(many=True, read_only=True)
    # tags = TagSerializer(many=True, read_only=True)

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
        # read_only_fields = RecipeSerializer.Meta.read_only_fields