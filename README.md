# Pratibha Kumari — Portfolio

A modern, responsive portfolio website for Pratibha Kumari, with a Python contact API that sends enquiries by email.

## Stack

- HTML5
- CSS3
- JavaScript
- Python serverless function
- SMTP / Gmail
- Vercel

## Deploy to Vercel

### 1. Upload to GitHub

Create a new GitHub repository and push this folder.

### 2. Import the repository into Vercel

In Vercel, choose **Add New → Project**, select the GitHub repository and deploy.

### 3. Add environment variables

In **Vercel → Project → Settings → Environment Variables**, add:

```text
SMTP_USER=your_gmail_address@gmail.com
SMTP_PASSWORD=your_gmail_app_password
CONTACT_TO_EMAIL=singhpratibha72963@gmail.com
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
```

`CONTACT_TO_EMAIL` is optional because the code already defaults to Pratibha's email.

### Gmail App Password

Do not put a normal Gmail password in Vercel.

For a Gmail account:
1. Enable 2-Step Verification.
2. Create a Google App Password.
3. Use that 16-character App Password as `SMTP_PASSWORD`.

## Important: text-file fallback

Vercel serverless functions do **not** provide persistent local storage, so simply writing enquiries to `responses.txt` is not a reliable production solution.

For production, the included email approach is recommended. If you later want a database-backed contact inbox, the API can be changed to MongoDB, PostgreSQL, Supabase, etc.

## Local test

You can preview the static site with:

```bash
python -m http.server 8000
```

However, the `/api/contact` Python endpoint requires a Vercel deployment (or a separate local Python server configured to run it).

## Customization

Edit:
- `index.html` for content
- `style.css` for design
- `script.js` for frontend behavior
- `api/contact.py` for email/contact handling
