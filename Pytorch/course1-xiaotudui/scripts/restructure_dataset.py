#!/usr/bin/env python3
"""
数据集重构脚本
将 hymenoptera_data 的原始结构:
    train/ants/*.jpg, train/bees/*.jpg
    val/ants/*.jpg, val/bees/*.jpg

重构为:
    ants_image/*.jpg + ants_label/*.txt
    bees_image/*.jpg + bees_label/*.txt

其中 label txt 文件名与图片名对应，内容为类别名（ants 或 bees）
"""

import os
import shutil
from pathlib import Path

# 配置路径
BASE_DIR = Path("/home/uav/Documents/Scientific_Study_Materials/deeplearning/PytorchLearning-Resources/course1:pytorch-xiaotudui")
SOURCE_DIR = BASE_DIR / "hymenoptera_data"
OUTPUT_DIR = BASE_DIR / "hymenoptera_data_restructured"

# 支持的图片格式
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}


def restructure_dataset():
    """重构数据集"""
    
    # 创建输出目录
    output_dirs = {
        'ants_image': OUTPUT_DIR / 'ants_image',
        'ants_label': OUTPUT_DIR / 'ants_label',
        'bees_image': OUTPUT_DIR / 'bees_image',
        'bees_label': OUTPUT_DIR / 'bees_label',
    }
    
    for dir_path in output_dirs.values():
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"创建目录: {dir_path}")
    
    # 统计计数
    stats = {'ants': 0, 'bees': 0}
    
    # 遍历 train 和 val 文件夹
    for split in ['train', 'val']:
        split_dir = SOURCE_DIR / split
        if not split_dir.exists():
            print(f"警告: {split_dir} 不存在，跳过")
            continue
        
        # 遍历 ants 和 bees 子文件夹
        for class_name in ['ants', 'bees']:
            class_dir = split_dir / class_name
            if not class_dir.exists():
                print(f"警告: {class_dir} 不存在，跳过")
                continue
            
            # 获取该类别的输出目录
            image_output_dir = output_dirs[f'{class_name}_image']
            label_output_dir = output_dirs[f'{class_name}_label']
            
            # 遍历所有图片
            for img_file in class_dir.iterdir():
                if img_file.suffix.lower() not in IMAGE_EXTENSIONS:
                    continue
                
                # 生成新文件名（加上 split 前缀避免重名）
                new_name = f"{split}_{img_file.name}"
                new_img_path = image_output_dir / new_name
                
                # 复制图片
                shutil.copy2(img_file, new_img_path)
                
                # 创建对应的标签文件
                label_filename = Path(new_name).stem + '.txt'
                label_path = label_output_dir / label_filename
                
                with open(label_path, 'w', encoding='utf-8') as f:
                    f.write(class_name)
                
                stats[class_name] += 1
    
    print("\n" + "=" * 50)
    print("重构完成!")
    print("=" * 50)
    print(f"蚂蚁图片数量: {stats['ants']}")
    print(f"蜜蜂图片数量: {stats['bees']}")
    print(f"\n输出目录: {OUTPUT_DIR}")
    print("\n目录结构:")
    print("  ├── ants_image/  (蚂蚁图片)")
    print("  ├── ants_label/  (蚂蚁标签txt，内容为'ants')")
    print("  ├── bees_image/  (蜜蜂图片)")
    print("  └── bees_label/  (蜜蜂标签txt，内容为'bees')")
    
    # 展示示例
    print("\n示例文件:")
    for class_name in ['ants', 'bees']:
        image_dir = output_dirs[f'{class_name}_image']
        label_dir = output_dirs[f'{class_name}_label']
        
        # 获取第一个文件作为示例
        images = list(image_dir.glob('*'))
        if images:
            sample_img = images[0]
            sample_label = label_dir / (sample_img.stem + '.txt')
            if sample_label.exists():
                with open(sample_label, 'r') as f:
                    label_content = f.read()
                print(f"  图片: {sample_img.name}")
                print(f"  标签: {sample_label.name} -> 内容: '{label_content}'")
                print()


if __name__ == "__main__":
    restructure_dataset()

