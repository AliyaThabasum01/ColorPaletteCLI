from palette import generate_palette

print("🎨 ColorPaletteCLI")
count = int(input("How many colors? "))

colors = generate_palette(count)

print("\nGenerated Palette\n")
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")
