"""
Week 1 - Basic Feature Class Loader & Inspector
arcpy-spatial-data-quality-pipeline

This script demonstrates:
- Connecting to data with ArcPy
- Using Describe() for rich metadata (very efficient)
- Getting feature counts and schema information
"""

import arcpy
from pathlib import Path

def inspect_feature_class(fc_path: str) -> None:
    """Inspect a feature class and print key metadata."""
    fc_path = str(Path(fc_path).resolve())  # Clean path handling

    if not arcpy.Exists(fc_path):
        print(f"❌ ERROR: Feature class does not exist at:\n{fc_path}")
        return

    print(f"\n{'='*70}")
    print(f"INSPECTING FEATURE CLASS")
    print(f"{'='*70}")
    print(f"Path: {fc_path}\n")

    desc = arcpy.Describe(fc_path)

    # Basic properties
    print(f"Name:              {desc.name}")
    print(f"Data Type:         {desc.dataType}")
    print(f"Shape Type:        {desc.shapeType}")
    print(f"Has Z Values:      {desc.hasZ}")
    print(f"Has M Values:      {desc.hasM}")

    # Spatial Reference (critical for later quality checks)
    sr = desc.spatialReference
    print(f"Spatial Reference: {sr.name} (WKID: {sr.factoryCode})")

    # Feature count
    count_result = arcpy.GetCount_management(fc_path)
    feature_count = int(count_result[0])
    print(f"Feature Count:     {feature_count:,}")

    # Fields
    fields = arcpy.ListFields(fc_path)
    print(f"\nFields ({len(fields)} total):")
    for field in fields:
        length_info = f", length={field.length}" if field.length else ""
        print(f"  • {field.name:<25} {field.type}{length_info}")

    print(f"\n{'='*70}\n")
    print("✅ Basic inspection complete.\n")


if __name__ == "__main__":
    # ====================== UPDATE THIS PATH ======================
    # Example paths (use raw string or forward slashes):
    # Shapefile:
    # fc_path = r"C:\Users\YourName\Documents\arcpy-spatial-data-quality-pipeline\data\denver_stormwater\Storm_Sewer_Mains.shp"
    
    # File Geodatabase feature class:
    # fc_path = r"C:\...\data\denver_stormwater\Denver_Stormwater.gdb\Storm_Sewer_Mains"
    
    fc_path = r"D:\Programing\arcpy-spatial-data-quality-pipeline\data\denver_stormwater\6898249d-ebab-4c4f-a58e-acae3c83cc0d.gdb\UTIL_STMMAIN_L"   # <-- Change this
    # ============================================================

    inspect_feature_class(fc_path)