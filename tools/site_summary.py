#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具模块：生成站点摘要信息
功能：读取内置站点资料并输出结构化摘要
"""

import json
from typing import Dict, List, Optional


class SiteInfo:
    """站点信息数据类"""

    def __init__(
        self,
        name: str,
        url: str,
        keywords: List[str],
        tags: List[str],
        description: str,
    ) -> None:
        self.name = name
        self.url = url
        self.keywords = keywords
        self.tags = tags
        self.description = description

    def to_dict(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "url": self.url,
            "keywords": self.keywords,
            "tags": self.tags,
            "description": self.description,
        }

    def __repr__(self) -> str:
        return f"SiteInfo(name={self.name!r}, url={self.url!r})"


class SiteSummaryGenerator:
    """生成站点结构化摘要"""

    def __init__(self, sites: Optional[List[SiteInfo]] = None) -> None:
        self.sites = sites if sites is not None else self._default_sites()

    def _default_sites(self) -> List[SiteInfo]:
        """内置默认站点资料"""
        return [
            SiteInfo(
                name="乐鱼体育",
                url="https://zhapp-leyu.com.cn",
                keywords=["乐鱼体育", "体育赛事", "直播"],
                tags=["体育", "娱乐", "在线"],
                description="乐鱼体育提供丰富的体育赛事直播和体育资讯服务。",
            ),
            SiteInfo(
                name="示例站点A",
                url="https://example-a.com",
                keywords=["示例", "测试", "工具"],
                tags=["demo", "example"],
                description="这是一个用于演示的站点，包含基础工具集。",
            ),
            SiteInfo(
                name="示例站点B",
                url="https://example-b.org",
                keywords=["帮助", "文档", "指南"],
                tags=["documentation", "tutorial"],
                description="提供各类技术文档和操作指南。",
            ),
        ]

    def generate_summaries(self) -> List[Dict[str, object]]:
        """生成所有站点的摘要列表"""
        return [site.to_dict() for site in self.sites]

    def generate_text_summary(self) -> str:
        """生成纯文本摘要"""
        lines = ["=== 站点结构化摘要 ==="]
        for idx, site in enumerate(self.sites, start=1):
            lines.append(f"[{idx}] 名称：{site.name}")
            lines.append(f"    URL：{site.url}")
            lines.append(f"    关键词：{', '.join(site.keywords)}")
            lines.append(f"    标签：{', '.join(site.tags)}")
            lines.append(f"    描述：{site.description}")
            lines.append("")
        return "\n".join(lines)

    def generate_json_summary(self, indent: int = 2) -> str:
        """生成JSON格式摘要"""
        data = {
            "generator": "SiteSummaryGenerator",
            "version": "1.0",
            "sites": self.generate_summaries(),
        }
        return json.dumps(data, ensure_ascii=False, indent=indent)


def main() -> None:
    """主入口：输出结构化摘要"""
    generator = SiteSummaryGenerator()

    # 输出纯文本摘要
    print(generator.generate_text_summary())

    # 输出JSON摘要
    print("--- JSON摘要 ---")
    print(generator.generate_json_summary(indent=4))


if __name__ == "__main__":
    main()