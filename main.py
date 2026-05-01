#!/usr/bin/env python3
"""Python Environment Health Checker — OBEDIENCE Tools"""
import sys, subprocess, importlib

CRITICAL = ["pip", "setuptools", "wheel"]
COMMON   = ["requests", "numpy", "pandas", "flask", "fastapi", "playwright"]

def check():
    results = {"ok": [], "missing": [], "broken": []}
    for pkg in CRITICAL + COMMON:
        try:
            importlib.import_module(pkg)
            results["ok"].append(pkg)
        except ImportError:
            results["missing"].append(pkg)
        except Exception as e:
            results["broken"].append(f"{pkg}: {e}")

    print(f"✅ OK ({len(results['ok'])}): {', '.join(results['ok'][:5])}...")
    if results["missing"]:
        print(f"❌ Missing: {', '.join(results['missing'])}")
        print(f"   Fix: pip install {' '.join(results['missing'])}")
    if results["broken"]:
        print(f"⚠️  Broken: {', '.join(results['broken'])}")
    return results

if __name__ == "__main__":
    check()
