import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Section
hero_target = """                <h2 class="title">Full Stack Developer | React · Ruby on Rails · Python</h2>
                <div
                    style="display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.3); color: #22c55e; padding: 0.4rem 1rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600; margin-bottom: 1rem;">
                    <span
                        style="width: 8px; height: 8px; background: #22c55e; border-radius: 50%; display: inline-block; animation: pulse 2s infinite;"></span>
                    Open to Work
                </div>
                <p class="bio">Passionate about building scalable web applications, automating workflows, and creating
                    dynamic user experiences. Currently Consultant at HashAgile Technologies.</p>"""

hero_replace = """                <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
                    <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(139,92,246,0.1); border: 1px solid rgba(139,92,246,0.3); color: #8b5cf6; padding: 0.4rem 1rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600;">
                        QA Automation Engineer
                    </div>
                    <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); color: #3b82f6; padding: 0.4rem 1rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600;">
                        Full Stack Developer
                    </div>
                    <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.3); color: #22c55e; padding: 0.4rem 1rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600;">
                        <span style="width: 8px; height: 8px; background: #22c55e; border-radius: 50%; display: inline-block; animation: pulse 2s infinite;"></span>
                        Open to Work
                    </div>
                </div>
                <p class="bio">I build scalable web applications and ensure their quality through comprehensive automated testing. Currently Consultant at HashAgile Technologies — writing code and the tests that prove it works.</p>"""
content = content.replace(hero_target, hero_replace)

# 2. Skills Section
skills_target = """                <!-- Programming -->
                <div class="skill-category glass-card fade-in-up">
                    <div class="category-icon"><i class="fas fa-code"></i></div>
                    <h3>Programming</h3>
                    <div class="skill-tags">
                        <span class="tag">Java</span>
                        <span class="tag">Python</span>
                        <span class="tag">C</span>
                    </div>
                </div>

                <!-- Frontend -->
                <div class="skill-category glass-card fade-in-up delay-1">
                    <div class="category-icon"><i class="fas fa-desktop"></i></div>
                    <h3>Frontend Development</h3>
                    <div class="skill-tags">
                        <span class="tag">React.js</span>
                        <span class="tag">Vue.js</span>
                        <span class="tag">JavaScript</span>
                        <span class="tag">HTML/CSS</span>
                        <span class="tag">Redux Toolkit</span>
                        <span class="tag">Bootstrap</span>
                        <span class="tag">Formik</span>
                    </div>
                </div>

                <!-- Backend & DB -->
                <div class="skill-category glass-card fade-in-up delay-2">
                    <div class="category-icon"><i class="fas fa-server"></i></div>
                    <h3>Backend & Database</h3>
                    <div class="skill-tags">
                        <span class="tag">Ruby on Rails</span>
                        <span class="tag">MySQL</span>
                        <span class="tag">PostgreSQL</span>
                        <span class="tag">REST APIs</span>
                    </div>
                </div>

                <!-- Tools & Others -->
                <div class="skill-category glass-card fade-in-up delay-3">
                    <div class="category-icon"><i class="fas fa-toolbox"></i></div>
                    <h3>Tools & OS</h3>
                    <div class="skill-tags">
                        <span class="tag">Linux</span>
                        <span class="tag">Git</span>
                        <span class="tag">Cypress</span>
                        <span class="tag">Playwright</span>
                        <span class="tag">Gen AI (ChatGPT, Claude, Gemini)</span>
                        <span class="tag">GitHub Copilot</span>
                    </div>
                </div>"""

skills_replace = """                <!-- QA & Automation -->
                <div class="skill-category glass-card fade-in-up" style="border-color: rgba(139,92,246,0.5); position: relative; overflow: hidden;">
                    <div style="position: absolute; top: 0.8rem; right: -2.2rem; background: var(--accent-purple); color: white; font-size: 0.6rem; font-weight: bold; padding: 0.2rem 2.5rem; transform: rotate(45deg);">PRIMARY</div>
                    <div class="category-icon"><i class="fas fa-check-double"></i></div>
                    <h3>QA & Automation</h3>
                    <div class="skill-tags">
                        <span class="tag">Cypress</span>
                        <span class="tag">Playwright</span>
                        <span class="tag">E2E Testing</span>
                        <span class="tag">Test Automation</span>
                        <span class="tag">LLM Validation</span>
                        <span class="tag">QA Frameworks</span>
                    </div>
                </div>

                <!-- Frontend -->
                <div class="skill-category glass-card fade-in-up delay-1">
                    <div class="category-icon"><i class="fas fa-desktop"></i></div>
                    <h3>Frontend Development</h3>
                    <div class="skill-tags">
                        <span class="tag">React.js</span>
                        <span class="tag">Vue.js</span>
                        <span class="tag">JavaScript</span>
                        <span class="tag">HTML/CSS</span>
                        <span class="tag">Redux Toolkit</span>
                        <span class="tag">Bootstrap</span>
                        <span class="tag">Formik</span>
                    </div>
                </div>

                <!-- Backend & DB -->
                <div class="skill-category glass-card fade-in-up delay-2">
                    <div class="category-icon"><i class="fas fa-server"></i></div>
                    <h3>Backend & Database</h3>
                    <div class="skill-tags">
                        <span class="tag">Java</span>
                        <span class="tag">Python</span>
                        <span class="tag">Ruby on Rails</span>
                        <span class="tag">MySQL</span>
                        <span class="tag">PostgreSQL</span>
                        <span class="tag">REST APIs</span>
                    </div>
                </div>

                <!-- Tools & AI -->
                <div class="skill-category glass-card fade-in-up delay-3">
                    <div class="category-icon"><i class="fas fa-toolbox"></i></div>
                    <h3>Tools & AI</h3>
                    <div class="skill-tags">
                        <span class="tag">Linux</span>
                        <span class="tag">Git</span>
                        <span class="tag">Gen AI (ChatGPT, Claude, Gemini)</span>
                        <span class="tag">GitHub Copilot</span>
                    </div>
                </div>"""
content = content.replace(skills_target, skills_replace)

# 3. Projects Filter Buttons
filter_target = """<h2 class="section-title fade-in">Featured <span class="text-accent">Projects</span></h2>"""
filter_replace = """<h2 class="section-title fade-in">Featured <span class="text-accent">Projects</span></h2>
            
            <div class="fade-in-up" style="display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem; flex-wrap: wrap;">
                <button class="btn btn-primary" style="padding: 0.5rem 1.5rem; font-size: 0.9rem;">All Projects</button>
                <button class="btn btn-outline" style="padding: 0.5rem 1.5rem; font-size: 0.9rem;">QA Automation</button>
                <button class="btn btn-outline" style="padding: 0.5rem 1.5rem; font-size: 0.9rem;">Full Stack</button>
            </div>"""
content = content.replace(filter_target, filter_replace)

# 4. Project Badges and Links
fs_badge = '<span style="background: rgba(59,130,246,0.1); color: #3b82f6; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; font-weight: 600; border: 1px solid rgba(59,130,246,0.2);">Full Stack</span>'
qa_badge = '<span style="background: rgba(139,92,246,0.1); color: #8b5cf6; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; font-weight: 600; border: 1px solid rgba(139,92,246,0.2);">QA Automation</span>'
fsa_badge = '<span style="background: rgba(20,184,166,0.1); color: #14b8a6; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; font-weight: 600; border: 1px solid rgba(20,184,166,0.2);">Full Stack · Automation</span>'

badges = {
    'IntelliChat': fs_badge,
    'Doorstep Mobile Service Platform': fs_badge,
    'Pre-Paid Energy Meter': fs_badge,
    'DeltaTrak UBQ': qa_badge,
    'LLM Bot Response Validator': qa_badge,
    'RPX License Manager': qa_badge,
    'Docx Data Extraction & Salesforce': fsa_badge
}

for proj, badge in badges.items():
    pattern = r'(<div class="project-header">)\s*(<i class="[^"]+"><\/i>)\s*(<h3>' + re.escape(proj) + r'<\/h3>)'
    def repl_header(m):
        icon = m.group(2).replace(' mb-3', '') # remove mb-3 from icon string if present
        return f'{m.group(1)}\n                            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">\n                                {icon}\n                                {badge}\n                            </div>\n                            {m.group(3)}'
    content = re.sub(pattern, repl_header, content)


content = re.sub(r'<h3>IntelliChat</h3>.*?<a href="#" target="_blank" class="text-accent"[^>]*><i\s*class="fab fa-github"></i> GitHub Repo</a>', 
                 lambda m: m.group(0).replace(re.search(r'<a href="#" target="_blank" class="text-accent"[^>]*><i\s*class="fab fa-github"></i> GitHub Repo</a>', m.group(0)).group(0), '<span class="text-accent" style="font-weight: 500; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 0.5rem; opacity: 0.6;">\n                                <i class="fas fa-lock"></i> Private Repository · HashAgile Technologies\n                            </span>'), content, flags=re.DOTALL)

content = re.sub(r'<h3>Pre-Paid Energy Meter</h3>.*?<a href="#" target="_blank" class="text-accent"[^>]*><i\s*class="fab fa-github"></i> GitHub Repo</a>', 
                 lambda m: m.group(0).replace(re.search(r'<a href="#" target="_blank" class="text-accent"[^>]*><i\s*class="fab fa-github"></i> GitHub Repo</a>', m.group(0)).group(0), '<span class="text-accent" style="font-weight: 500; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 0.5rem; opacity: 0.6;">\n                                <i class="fas fa-lock"></i> Academic Project\n                            </span>'), content, flags=re.DOTALL)

content = re.sub(r'<h3>Doorstep Mobile Service Platform</h3>.*?<a href="#" target="_blank" class="text-accent"[^>]*><i\s*class="fab fa-github"></i> GitHub Repo</a>', 
                 lambda m: m.group(0).replace(re.search(r'<a href="#" target="_blank" class="text-accent"[^>]*><i\s*class="fab fa-github"></i> GitHub Repo</a>', m.group(0)).group(0), '<span class="text-accent" style="font-weight: 500; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 0.5rem; opacity: 0.6;">\n                                <i class="fas fa-lock"></i> Personal Project\n                            </span>'), content, flags=re.DOTALL)

# 5. About Section Paragraph & Stat Cards
about_target = """                <p class="desc text-light"
                    style="font-size: 1.1rem; line-height: 1.8; max-width: 800px; margin: 0 auto;">
                    Full Stack Developer with hands-on experience in React, Vue.js, Ruby on Rails, and Python. Currently
                    working as a Consultant at HashAgile Technologies, where I build automation tools and Salesforce
                    integrations. I'm passionate about AI-powered applications and scalable web solutions. Open to
                    full-time opportunities.
                </p>"""

about_replace = """                <p class="desc text-light"
                    style="font-size: 1.1rem; line-height: 1.8; max-width: 800px; margin: 0 auto; margin-bottom: 3rem;">
                    I bring a unique combination of QA Automation and Full Stack development — I can build scalable web applications and ensure their quality through comprehensive automated testing frameworks. Open to full-time opportunities in QA Automation or Full Stack roles.
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; max-width: 900px; margin: 0 auto;">
                    <div class="glass-card" style="padding: 1.5rem; text-align: center;">
                        <h4 style="font-size: 2rem; color: var(--accent-purple); margin-bottom: 0.5rem;">1+</h4>
                        <p style="color: var(--text-secondary); font-size: 0.9rem;">Year Experience</p>
                    </div>
                    <div class="glass-card" style="padding: 1.5rem; text-align: center;">
                        <h4 style="font-size: 2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">7+</h4>
                        <p style="color: var(--text-secondary); font-size: 0.9rem;">Projects Built</p>
                    </div>
                    <div class="glass-card" style="padding: 1.5rem; text-align: center;">
                        <h4 style="font-size: 2rem; color: var(--accent-purple); margin-bottom: 0.5rem;">2</h4>
                        <p style="color: var(--text-secondary); font-size: 0.9rem;">Test Frameworks</p>
                    </div>
                    <div class="glass-card" style="padding: 1.5rem; text-align: center;">
                        <h4 style="font-size: 2rem; color: var(--accent-blue); margin-bottom: 0.5rem;">5+</h4>
                        <p style="color: var(--text-secondary); font-size: 0.9rem;">Tech Stacks</p>
                    </div>
                </div>"""
if about_target in content:
    content = content.replace(about_target, about_replace)

# 6. Footer
footer_target = """                <div class="social-links">
                    <a href="https://www.linkedin.com/in/sairam-achanta-a22b17199" target="_blank"><i
                            class="fab fa-linkedin-in"></i></a>
                    <a href="mailto:sairamachanta1433@gmail.com"><i class="fas fa-envelope"></i></a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Sai Ram Achanta. Designed & Built with ❤️.</p>
            </div>"""

footer_replace = """                <div class="social-links">
                    <a href="https://www.linkedin.com/in/sairam-achanta-a22b17199" target="_blank"><i
                            class="fab fa-linkedin-in"></i></a>
                    <a href="https://github.com/sairamachanta" target="_blank"><i class="fab fa-github"></i></a>
                    <a href="mailto:sairamachanta1433@gmail.com"><i class="fas fa-envelope"></i></a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Sai Ram Achanta. QA Automation Engineer & Full Stack Developer.</p>
            </div>"""
if footer_target in content:
    content = content.replace(footer_target, footer_replace)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done modification!")
