
import sys
import subprocess
import importlib.util

def check_package_installation():
    """Verify all required packages are properly installed."""
    
    required_packages = {
        'openai': '1.37.2',
        'telnyx': '2.0.0', 
        'aiohttp': '3.10.10',
        'python-dotenv': '1.0.1',
        'psutil': '6.1.0',
        'asyncio-throttle': '1.0.2',
        'cryptography': '43.0.3',
        'pydantic': '2.8.2',
        'structlog': '24.4.0'
    }
    
    voice_packages = {
        'pipecat': 'pipecat-ai',
        'elevenlabs': 'elevenlabs'
    }
    
    print("🔍 PACKAGE VERIFICATION REPORT")
    print("=" * 50)
    
    # Check required packages
    print("\n✅ REQUIRED PACKAGES:")
    all_required_ok = True
    
    for package, expected_version in required_packages.items():
        try:
            spec = importlib.util.find_spec(package)
            if spec is not None:
                # Try to get version
                try:
                    if package == 'python-dotenv':
                        import dotenv
                        version = dotenv.__version__
                    else:
                        module = importlib.import_module(package)
                        version = getattr(module, '__version__', 'Unknown')
                    print(f"   ✅ {package}: {version}")
                except:
                    print(f"   ✅ {package}: Installed (version check failed)")
            else:
                print(f"   ❌ {package}: NOT FOUND")
                all_required_ok = False
        except Exception as e:
            print(f"   ❌ {package}: ERROR - {e}")
            all_required_ok = False
    
    # Check voice packages
    print("\n🔧 VOICE AI PACKAGES:")
    voice_packages_ok = True
    
    for package, pip_name in voice_packages.items():
        try:
            spec = importlib.util.find_spec(package)
            if spec is not None:
                try:
                    module = importlib.import_module(package)
                    version = getattr(module, '__version__', 'Unknown')
                    print(f"   ✅ {package}: {version}")
                except:
                    print(f"   ✅ {package}: Installed (version check failed)")
            else:
                print(f"   ❌ {package}: NOT FOUND - Run: pip install {pip_name}")
                voice_packages_ok = False
        except Exception as e:
            print(f"   ❌ {package}: ERROR - {e}")
            voice_packages_ok = False
    
    # Overall status
    print("\n" + "=" * 50)
    print("📊 INSTALLATION STATUS:")
    
    if all_required_ok:
        print("   ✅ Core Dependencies: READY")
    else:
        print("   ❌ Core Dependencies: INCOMPLETE")
    
    if voice_packages_ok:
        print("   ✅ Voice AI Packages: READY")
        print("   🚀 STATUS: READY FOR VOICE AGENT DEVELOPMENT")
    else:
        print("   ⚠️  Voice AI Packages: INCOMPLETE")
        print("   🔧 STATUS: REQUIRES ADDITIONAL INSTALLATION")
    
    return all_required_ok and voice_packages_ok

def test_basic_functionality():
    """Test basic functionality of key packages."""
    
    print("\n🧪 FUNCTIONALITY TESTS:")
    print("=" * 30)
    
    # Test OpenAI import
    try:
        import openai
        print("   ✅ OpenAI: Import successful")
    except Exception as e:
        print(f"   ❌ OpenAI: {e}")
    
    # Test Telnyx import
    try:
        import telnyx
        print("   ✅ Telnyx: Import successful")
    except Exception as e:
        print(f"   ❌ Telnyx: {e}")
    
    # Test aiohttp
    try:
        import aiohttp
        print("   ✅ aiohttp: Import successful")
    except Exception as e:
        print(f"   ❌ aiohttp: {e}")
    
    # Test environment loading
    try:
        from dotenv import load_dotenv
        print("   ✅ python-dotenv: Import successful")
    except Exception as e:
        print(f"   ❌ python-dotenv: {e}")
    
    # Test PipeCat
    try:
        import pipecat
        print("   ✅ PipeCat: Import successful")
    except Exception as e:
        print(f"   ❌ PipeCat: {e}")
    
    # Test ElevenLabs
    try:
        import elevenlabs
        print("   ✅ ElevenLabs: Import successful")
    except Exception as e:
        print(f"   ❌ ElevenLabs: {e}")

def create_sample_env_file():
    """Create a sample .env file with Polish voice agent configuration."""
    
    env_content = '''# Polish Voice Agent Configuration
# ==========================================

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# ElevenLabs Configuration  
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM  # Polish voice

# Telnyx Configuration
TELNYX_API_KEY=your_telnyx_api_key_here
TELNYX_PUBLIC_KEY=your_telnyx_public_key_here

# Polish Language Settings
LANGUAGE=pl
COUNTRY_CODE=PL
VOICE_LANGUAGE=pl-PL

# Application Settings
DEBUG=true
LOG_LEVEL=INFO
AUDIO_SAMPLE_RATE=16000
AUDIO_CHANNELS=1

# Cost Optimization
MAX_TOKENS=150
TEMPERATURE=0.7
'''
    
    try:
        with open('.env.example', 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("\n📄 Created .env.example file with Polish voice agent configuration")
        print("   Copy this to .env and add your API keys")
    except Exception as e:
        print(f"\n❌ Failed to create .env.example: {e}")

if __name__ == "__main__":
    print("🎯 POLISH VOICE AGENT - INSTALLATION VERIFICATION")
    print("=" * 60)
    print(f"Python Version: {sys.version}")
    print(f"Python Path: {sys.executable}")
    
    # Run verification
    installation_ok = check_package_installation()
    test_basic_functionality()
    create_sample_env_file()
    
    print("\n" + "=" * 60)
    if installation_ok:
        print("🎉 VERIFICATION COMPLETE: Ready for voice agent development!")
        print("\n🚀 NEXT STEPS:")
        print("   1. Copy .env.example to .env")
        print("   2. Add your API keys to .env")
        print("   3. Start building your Polish voice agent!")
    else:
        print("⚠️  VERIFICATION INCOMPLETE: Some packages need attention.")
