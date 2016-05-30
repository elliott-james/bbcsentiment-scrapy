BOT_NAME = 'bbc'

SPIDER_MODULES = ['bbc.spiders']
NEWSPIDER_MODULE = 'bbc.spiders'

MIN_ARTICLE_LENGTH = 1

ITEM_PIPELINES = {
    'bbc.pipelines.ExtractArticlePipeline',
    'bbc.pipelines.DropShortArticlesPipeline',
    'bbc.pipelines.SentimentPipeline'
}