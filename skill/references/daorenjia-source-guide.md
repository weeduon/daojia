# Daorenjia source guide

## Contents

- Scope and provenance
- Canonical entry points
- Category map
- Retrieval workflow
- Interpretation limits

## Scope and provenance

Base URL: <https://www.daorenjia.com/>

The site describes itself as an online reading collection organized around the 49-volume modern compilation 《中华道藏》 and the traditional 三洞四辅 framework. Its home page says the collection contains more than 1,500 works and 5,500 scrolls in the source compilation.

The site's About page states:

- source images were obtained as DJVU files;
- much text was initially collected from other websites;
- the maintainer compares and corrects transcriptions manually against the DJVU edition;
- pages marked `已校对` or `校对一次` have received the site's stated checking;
- the web text may replace some traditional characters with common variants;
- `◇` replaces a missing-character square in the source;
- some textual-variant notes were removed from the web transcription, so consult the image version when those notes matter.

No clear open-content license was found during integration. Treat the site as an external locator and transcription source. Do not bundle the entire website.

Integration snapshot generated on 2026-07-28:

- 24 leaf categories indexed;
- 1,524 unique work records;
- 591 records matched the site's own `已校对` index;
- full scripture bodies are intentionally not bundled.

## Canonical entry points

- Home: <https://www.daorenjia.com/>
- About and transcription notes: <https://www.daorenjia.com/about.php>
- Directory: <https://www.daorenjia.com/mulu>
- Site-marked checked texts: <https://www.daorenjia.com/yjd>
- Search: <https://www.daorenjia.com/search>

## Category map

| Group | Category | URL |
| --- | --- | --- |
| 三洞真经 | 三洞真经总览 | <https://www.daorenjia.com/c1> |
| 三洞真经 | 洞真上清经 | <https://www.daorenjia.com/c8> |
| 三洞真经 | 洞玄灵宝经 | <https://www.daorenjia.com/c9> |
| 三洞真经 | 洞神三皇经 | <https://www.daorenjia.com/c10> |
| 三洞真经 | 三洞经教 | <https://www.daorenjia.com/c11> |
| 四辅真经 | 四辅真经总览 | <https://www.daorenjia.com/c2> |
| 四辅真经 | 太平部诸经 | <https://www.daorenjia.com/c12> |
| 四辅真经 | 太玄部经诀 | <https://www.daorenjia.com/c13> |
| 四辅真经 | 正一部经籙 | <https://www.daorenjia.com/c14> |
| 四辅真经 | 道德真经 | <https://www.daorenjia.com/c15> |
| 四辅真经 | 四子真经 | <https://www.daorenjia.com/c16> |
| 四辅真经 | 黄帝阴符经 | <https://www.daorenjia.com/c17> |
| 四辅真经 | 道教易学 | <https://www.daorenjia.com/c18> |
| 四辅真经 | 太清金丹经 | <https://www.daorenjia.com/c19> |
| 四辅真经 | 太清摄养经 | <https://www.daorenjia.com/c20> |
| 道教论集 | 道教论集总览 | <https://www.daorenjia.com/c3> |
| 道教论集 | 诸子文集 | <https://www.daorenjia.com/c21> |
| 道教论集 | 道学论著 | <https://www.daorenjia.com/c22> |
| 道教论集 | 全真文集 | <https://www.daorenjia.com/c23> |
| 道教论集 | 道教类书 | <https://www.daorenjia.com/c24> |
| 道法众术 | 道法众术总览 | <https://www.daorenjia.com/c4> |
| 道法众术 | 道法诸经 | <https://www.daorenjia.com/c25> |
| 道法众术 | 道法总集 | <https://www.daorenjia.com/c26> |
| 道教科仪 | 道教科仪总览 | <https://www.daorenjia.com/c5> |
| 道教科仪 | 科戒威仪 | <https://www.daorenjia.com/c27> |
| 道教科仪 | 灵宝诸斋仪 | <https://www.daorenjia.com/c28> |
| 道教科仪 | 灯仪法忏章表 | <https://www.daorenjia.com/c29> |
| 道史仙传 | 道史仙传总览 | <https://www.daorenjia.com/c6> |
| 道史仙传 | 神仙高道传 | <https://www.daorenjia.com/c30> |
| 道史仙传 | 仙境名山志 | <https://www.daorenjia.com/c31> |

## Retrieval workflow

1. Search `daorenjia-catalog.tsv` with the exact title and one or two short variants.
2. Prefer an exact title match; distinguish base text, commentary, annotation, ritual adaptation, and similarly named works.
3. Open the record's canonical URL.
4. Capture:
   - breadcrumb category;
   - displayed title;
   - introductory bibliographic note;
   - `已校对`/`校对一次` status;
   - scroll/chapter location;
   - whether an image edition is linked;
   - exact passage needed for the current question.
5. If wording, characters, diagrams, talismans, or textual variants matter, inspect the image version.
6. Cross-check an independent source before making a strong historical, doctrinal, medical, or ritual claim.
7. Cite the individual work page, not only the home page or search page.

When browsing is unavailable, use the catalog only to identify likely works and state that the passage has not been inspected.

## Interpretation limits

- Inclusion in the collection does not prove current universal practice.
- A scripture's self-attribution is not automatically its historical authorship.
- Introductory metadata can contain traditional attribution and should be distinguished from academic dating.
- A site correction label does not eliminate OCR, transcription, punctuation, or edition errors.
- Web transcriptions may omit illustrations, seals, diagrams, layout, marginal notes, or variant readings.
- Do not reconstruct missing talismanic graphs or rare characters from context alone.
