#!/usr/bin/env python3
"""
Quick test to verify all packages are working correctly for Polish Voice Agent
"""

import sys
import importlib

def test_package(package_name, import_name=None):
    """Test if a package can be imported successfully"""
    if import_name is None:
        import_name = package_name
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {package_name}: Working correctly")
        return True
    except ImportError as e:
        print(f"❌ {package_name}: Import failed - {e}")
        return False

def main():
    print("🧪 POLISH VOICE AGENT - PACKAGE FUNCTIONALITY TEST")
    print("=" * 55)
    
    packages_to_test = [
        ("python-dotenv", "dotenv"),
        ("asyncio-throttle", "asyncio_throttle"),
        ("openai", "openai"),
        ("elevenlabs", "elevenlabs"),
        ("telnyx", "telnyx"),
        ("pipecat", "pipecat"),
        ("aiohttp", "aiohttp"),
        ("psutil", "psutil"),
        ("cryptography", "cryptography"),
        ("pydantic", "pydantic"),
        ("structlog", "structlog"),
    ]
    
    all_working = True
    working_count = 0
    total_count = len(packages_to_test)
    
    for package_name, import_name in packages_to_test:
        if test_package(package_name, import_name):
            working_count += 1
        else:
            all_working = False
    
    print("
" + "=" * 55)
    print(f"📊 RESULTS: {working_count}/{total_count} packages working")
    
    if all_working:
        print("🎉 ALL PACKAGES WORKING! Your Polish Voice Agent is ready!")
        print("
📋 Next steps:")
        print("   1. Copy .env.example to .env")
        print("   2. Add your API keys to .env")
        print("   3. Run: python polish_voice_agent.py")
    elif working_count >= 7:  # Core packages working
        print("🚀 CORE PACKAGES WORKING! Voice agent is functional!")
        print(f"
⚠️  {total_count - working_count} optional packages missing")
        print("   You can still run your voice agent with core functionality")
        print("
📋 To install missing packages:")
        print("   pip install asyncio-throttle")
    else:
        print("⚠️  Some core packages need attention. Run the fix script.")
    
    return all_working

if __name__ == "__main__":
    main()
