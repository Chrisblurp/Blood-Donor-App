import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloodBackend.local_settings')
django.setup()

from django.urls import get_resolver

print("=== All URL Patterns ===\n")
resolver = get_resolver()
for i, pattern in enumerate(resolver.url_patterns):
    print(f"{i}: {pattern.pattern}")
    if hasattr(pattern, 'url_patterns'):
        for j, subpattern in enumerate(pattern.url_patterns):
            print(f"  {j}: {subpattern.pattern}")

print("\n=== Checking for metrics ===\n")
found_metrics = False
for pattern in resolver.url_patterns:
    if 'metrics' in str(pattern.pattern):
        print(f"✓ Found metrics pattern: {pattern.pattern}")
        found_metrics = True
    if hasattr(pattern, 'url_patterns'):
        for subpattern in pattern.url_patterns:
            if 'metrics' in str(subpattern.pattern):
                print(f"✓ Found metrics subpattern: {subpattern.pattern}")
                found_metrics = True

if not found_metrics:
    print("✗ No metrics pattern found!")
