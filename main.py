from verifier import verify_biometric

base_sample = "AGTTGACCTTGGA"
input_sample = "AGTTGACCTTGGG"

similarity, verified = verify_biometric(base_sample, input_sample)

print(f"Similarity: {similarity:.2f}")
print("Verified Identify" if verified else "Not Match")


