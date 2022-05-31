from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Follow, Group, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')
        read_only_fields = ('title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),)

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Нельзя подписываться на себя!'
            )
        ]

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return data
