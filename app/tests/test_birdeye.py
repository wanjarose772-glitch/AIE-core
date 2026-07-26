from app.collectors.birdeye import BirdEyeCollector

collector = BirdEyeCollector()

data = collector.trending_tokens(10)

print(data)