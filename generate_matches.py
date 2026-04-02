with open('highlighted_results.txt', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

html_snippets = []
current_match = ""
t1 = ""
t2 = ""
sim = ""

for line in lines:
    line = line.strip()
    if not line: continue
    if line.startswith('Match'):
        current_match = line.strip()
    elif line.startswith('Text1:'):
        t1 = line.replace('Text1:', '').strip()
    elif line.startswith('Text2:'):
        t2 = line.replace('Text2:', '').strip()
    elif line.startswith('Similarity:'):
        sim = line.replace('Similarity:', '').strip()
        block = f'''                        <div class="box" style="margin-bottom: 2rem; border: 1px solid #ddd; background-color: #fafafa;">
                            <h5 class="title is-5 has-text-grey" style="margin-bottom: 1rem;">{current_match} <span class="tag is-info is-light is-pulled-right">Similarity: {sim}</span></h5>
                            <div class="columns">
                                <div class="column is-half" style="border-right: 1px solid #eee;">
                                    <h6 class="subtitle is-6">Original Text (Text 1)</h6>
                                    <p class="is-size-6" style="line-height: 1.6;">{t1}</p>
                                </div>
                                <div class="column is-half">
                                    <h6 class="subtitle is-6">Recovered Text (Text 2)</h6>
                                    <p class="is-size-6" style="line-height: 1.6;">{t2}</p>
                                </div>
                            </div>
                        </div>'''
        html_snippets.append(block)

final_html = '\n'.join(html_snippets)
final_html = final_html.replace('<font color="red">', '<span class="has-text-danger has-text-weight-bold">').replace('</font>', '</span>')

wrapper = f'''                    <div id="text-results-container" class="content" style="max-height: 500px; overflow-y: auto; padding: 1.5rem; border: 1px solid #eee; border-radius: 8px; background-color: #fff; box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);">
{final_html}
                    </div>'''

with open('compiled_html.txt', 'w', encoding='utf-8') as f:
    f.write(wrapper)
