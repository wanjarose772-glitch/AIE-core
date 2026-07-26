from packages.intelligence.token_intelligence import get_token_metadata

mint = "Bkm1PqGWCdG9MLCSidZ6wDwrDaQPhf3fYdxK3y9Qpump"

metadata = get_token_metadata(mint)

print()
print("=" * 60)
print("TOKEN METADATA")
print("=" * 60)

for key, value in metadata.items():
    print(f"{key}: {value}")