from django.contrib.syndication.views import Feed
from myblog.models import Post


class LatestEntriesFeed(Feed):
	title = "Latest Posts"
	link = "/latest/feed"
	description = "Updates on changes and additions to blog posts"

	def items(self):
		return Post.objects.order_by('published_date')[:5]

	def item_title(self, item):
		return item.title
