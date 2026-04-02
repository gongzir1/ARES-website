html_snippets = []
for i in range(32):
    block = f'''                        <div class="box" style="margin-bottom: 2rem; border: 1px solid #ddd; background-color: #fafafa;">
                            <h5 class="title is-5 has-text-grey" style="margin-bottom: 1rem;">Audio Example {i}</h5>
                            <div class="columns">
                                <div class="column is-half" style="border-right: 1px solid #eee;">
                                    <h6 class="subtitle is-6 has-text-centered">Original Audio</h6>
                                    <audio controls style="width: 100%;">
                                        <source src="https://raw.githubusercontent.com/gongzir1/ARES/main/AudioExample/run_0/ground_truth/groundtruth_{i}.wav" type="audio/wav">
                                        Your browser does not support the audio element.
                                    </audio>
                                </div>
                                <div class="column is-half">
                                    <h6 class="subtitle is-6 has-text-centered">Recovered Audio</h6>
                                    <audio controls style="width: 100%;">
                                        <source src="https://raw.githubusercontent.com/gongzir1/ARES/main/AudioExample/run_0/recovered/recovered_{i}.wav" type="audio/wav">
                                        Your browser does not support the audio element.
                                    </audio>
                                </div>
                            </div>
                        </div>'''
    html_snippets.append(block)

final_html = '\n'.join(html_snippets)

wrapper = f'''                    <hr style="margin-top: 3rem; margin-bottom: 3rem;">
                    
                    <h3 class="title is-4 has-text-centered" style="margin-bottom: 2rem;">Audio Reconstruction</h3>
                    <p class="has-text-centered" style="margin-bottom: 2rem;">
                        ARES extends beyond images and text, maintaining high fidelity in audio reconstruction tasks. Below are side-by-side comparisons of the original ground truth audio against the recovered audio from gradient data.
                    </p>

                    <div id="audio-results-container" class="content" style="max-height: 500px; overflow-y: auto; padding: 1.5rem; border: 1px solid #eee; border-radius: 8px; background-color: #fff; box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);">
{final_html}
                    </div>'''

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

new_lines = lines[:1147] + wrapper.splitlines() + lines[1147:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
