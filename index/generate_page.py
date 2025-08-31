# The final script to generate your production-ready index.html file.

def create_final_page(background_url, logo_url, instagram_url, facebook_url, linkedin_url, output_file="index.html"):
    """Generates the final, self-contained HTML file with online image links."""

    # --- Your Links ---
    dossier_sponsoring = "https://drive.google.com/file/d/1ibzMJqappOLsiiiK4i_zU252Mmof-idq/view?usp=sharing"
    website = "https://rtc.ieee.tn"
    facebook_page = "https://www.facebook.com/share/1GCPaKanBz/"
    trsyp_instagram = "https://www.instagram.com/ieee_trsyp"
    linkedin_page = "https://www.linkedin.com/company/ieee-ras-tunisia-section/"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IEEE TRSYP Links</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Orbitron:wght@800&display=swap" rel="stylesheet">
        
        <style>
            :root {{
                --primary-blue: #2271B6; --secondary-green: #23B5A8; --text-light: #f8f9fa;
                --instagram-glow: rgba(228, 64, 95, 0.7); --facebook-glow: rgba(24, 119, 242, 0.7); --linkedin-glow: rgba(10, 102, 194, 0.7);
            }}
            body {{
                font-family: 'Montserrat', sans-serif; color: var(--text-light);
                background-image: url('{background_url}'); 
                background-size: cover; background-position: center center; background-attachment: fixed; padding: 1rem;
            }}
            .main-container {{ min-height: calc(100vh - 2rem); display: flex; align-items: center; justify-content: center; }}
            .glass-card {{
                background: rgba(10, 10, 20, 0.8); backdrop-filter: blur(15px) saturate(180%); -webkit-backdrop-filter: blur(15px) saturate(180%);
                border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.125); padding: 2.5rem 1.5rem;
                max-width: 600px; width: 100%; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            }}
            .profile-img {{ width: 140px; height: 140px; border-radius: 50%; border: 4px solid var(--primary-blue); margin-top: -95px; margin-bottom: 1rem; background-color: #000; }}
            .profile-title {{ font-family: 'Orbitron', sans-serif; font-weight: 800; font-size: clamp(2.5rem, 8vw, 3rem); color: var(--text-light); text-shadow: 0 0 15px rgba(34, 113, 182, 0.5); }}
            .profile-description {{ font-size: 1rem; color: #ced4da; margin-bottom: 2rem; max-width: 450px; margin-left: auto; margin-right: auto; }}
            .social-icons {{ display: flex; justify-content: center; align-items: center; gap: 1.5rem; }}
            .social-icons a {{ display: flex; align-items: center; justify-content: center; width: 60px; height: 60px; border-radius: 50%; transition: all 0.3s ease-in-out; }}
            .social-icons img {{ width: 48px; height: 48px; transition: transform 0.3s ease; }}
            .social-icons a:hover {{ transform: translateY(-5px); }}
            .social-icons a:hover img {{ transform: scale(1.1); }}
            .icon-instagram:hover {{ box-shadow: 0 0 20px 5px var(--instagram-glow); }}
            .icon-facebook:hover {{ box-shadow: 0 0 20px 5px var(--facebook-glow); }}
            .icon-linkedin:hover {{ box-shadow: 0 0 20px 5px var(--linkedin-glow); }}
            .link-btn {{ background: transparent; border: 2px solid var(--primary-blue); color: var(--text-light); font-weight: 600; font-size: 1.1rem; padding: 1rem; transition: all 0.3s ease; }}
            .link-btn:hover {{ background: var(--primary-blue); border-color: var(--secondary-green); color: var(--text-light); transform: scale(1.05); }}
            .footer-text {{ font-size: 0.8rem; color: #6c757d; margin-top: 2rem; padding-bottom: 0; }}
        </style>
    </head>
    <body>
        <div class="container main-container">
            <div class="glass-card text-center">
                <img src="{logo_url}" alt="TRSYP Logo" class="profile-img">
                <h1 class="profile-title">TRSYP</h1>
                <p class="profile-description">An annual event that gathers IEEE RAS Tunisia Section members, organized by the IEEE ENET’Com Student Branch and IEEE RAS ENET’Com Student Branch Chapter.</p>
                <div class="social-icons mb-4">
                    <a href="{trsyp_instagram}" target="_blank" title="Instagram" class="icon-instagram"><img src="{instagram_url}" alt="Instagram"></a>
                    <a href="{facebook_page}" target="_blank" title="Facebook" class="icon-facebook"><img src="{facebook_url}" alt="Facebook"></a>
                    <a href="{linkedin_page}" target="_blank" title="LinkedIn" class="icon-linkedin"><img src="{linkedin_url}" alt="LinkedIn"></a>
                </div>
                <div class="d-grid gap-3 mt-4">
                    <a href="{website}" class="btn link-btn" target="_blank">Official Website</a>
                    <a href="{dossier_sponsoring}" class="btn link-btn" target="_blank">Sponsoring Dossier</a>
                </div>
                <p class="footer-text">© 2025 IEEE TRSYP. All Rights Reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully created final '{output_file}' with online image links.")

if __name__ == "__main__":
    # --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    # --- All 5 links are now filled in and ready to use! ---
    # --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    BACKGROUND_URL = "https://i.postimg.cc/svrM31LN/t-01.png"
    LOGO_URL       = "https://i.postimg.cc/DShLpxFm/PDP-Final-4x.png"
    
    # Using public, reliable links for the brand icons
    INSTAGRAM_URL  = "https://i.postimg.cc/q77Qv3mP/instagram.png" # A reliable public link for the Instagram icon
    FACEBOOK_URL   = "https://i.postimg.cc/d1y3z65p/facebook.png" # A reliable public link for the Facebook icon
    
    LINKEDIN_URL   = "https://i.postimg.cc/KRBt5d6d/linkedin.png"

    create_final_page(BACKGROUND_URL, LOGO_URL, INSTAGRAM_URL, FACEBOOK_URL, LINKEDIN_URL)