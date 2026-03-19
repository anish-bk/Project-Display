"""
Museum Data Loader

Scans the BG_removed_ouptuts_hunyuan folder structure
and returns structured data for the gallery and results templates.

Structure:
  BG_removed_ouptuts_hunyuan/
    kanha/
      Kanha_nobg.png
      Kanha_1/
        input.png
        textured_mesh.glb
        ...
      Kanha_2/
        ...
      ...Kanha_20/
"""

import os
from django.conf import settings


def get_museum_artifacts():
    """
    Returns a list of artifact dicts, one per top-level folder (artwork).
    Each dict contains:
      - name: display name (folder name)
      - slug: URL safe name
      - nobg_image: path to background-removed image  (relative to static)
      - input_image: path to original input image from iteration_1 (relative to static)
      - iterations: list of iteration dicts, each with:
          - number: iteration number
          - glb_path: path to textured_mesh.glb (relative to static)
          - input_path: path to input.png (relative to static)
    """
    base_dir = os.path.join(settings.STATICFILES_DIRS[0], 'museum_assets')

    if not os.path.isdir(base_dir):
        return []

    artifacts = []

    for folder_name in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.isdir(folder_path):
            continue

        # Build display name
        display_name = folder_name.replace('_', ' ').title()

        # Build slug (URL-safe)
        slug = folder_name.lower().replace(' ', '_')

        # Find nobg image
        nobg_image = None
        for f in os.listdir(folder_path):
            if f.lower().endswith('_nobg.png') or f.lower() == 'nobg.png':
                nobg_image = f'museum_assets/{folder_name}/{f}'
                break

        # Collect iterations
        iterations = []
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if not os.path.isdir(item_path):
                continue

            # Parse iteration number from folder name like "Kanha_1", "Kanha_20"
            parts = item.rsplit('_', 1)
            if len(parts) != 2:
                continue
            try:
                iter_num = int(parts[1])
            except ValueError:
                continue

            # Find textured_mesh.glb
            glb_path = None
            input_path = None

            for file_name in os.listdir(item_path):
                if file_name == 'textured_mesh.glb':
                    glb_path = f'museum_assets/{folder_name}/{item}/{file_name}'
                elif file_name == 'input.png':
                    input_path = f'museum_assets/{folder_name}/{item}/{file_name}'

            if glb_path:
                iterations.append({
                    'number': iter_num,
                    'glb_path': glb_path,
                    'input_path': input_path,
                })

        iterations.sort(key=lambda x: x['number'])

        # Use the first iteration's input image as the main input
        input_image = iterations[0]['input_path'] if iterations else None

        # Use the last iteration's glb as the "best" reconstruction
        best_glb = iterations[-1]['glb_path'] if iterations else None

        artifact = {
            'name': display_name,
            'slug': slug,
            'nobg_image': nobg_image,
            'input_image': input_image,
            'best_glb': best_glb,
            'iterations': iterations,
            'iteration_count': len(iterations),
        }
        artifacts.append(artifact)

    return artifacts
