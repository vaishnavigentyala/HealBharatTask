# ⏱️ Increaser

A comprehensive productivity toolkit that empowers knowledge workers to boost focus, achieve meaningful goals, and create a perfect work-life balance.

## 🚀 What is Increaser?

Increaser is your personal productivity companion that helps you transform how you work! Structure your work into focused sessions, track time across projects, build rock-solid habits, manage tasks effortlessly, and align your daily work with your long-term vision.

## ✨ Key Features

- **⏳ Focus Sessions**: Supercharge your productivity with timed focus sessions, smart breaks, and the science-backed 90-minute work block system
- **🔮 Vision Board**: Visualize your ideal life with inspiring life aspirations that keep you motivated
- **🎯 Goals Tracking**: Set concrete, measurable goals with deadlines and watch your progress unfold
- **📊 Project Management**: Organize work with smart time budgets and crystal-clear goals
- **🔄 Habit Tracking**: Build life-changing daily habits with motivating streak tracking
- **✅ Task Management**: Conquer your to-dos with an intuitive Kanban board, powerful recurring task automation, and time-saving templates
- **📝 Principles**: Document your guiding principles for a more intentional, fulfilling life
- **📈 Timesheet**: Gain powerful insights into how you spend your time across projects

## 👥 Who It's For

Increaser is designed for programmers, designers, marketers, engineers, students, and other knowledge workers who want to level up their productivity. It's especially valuable for remote workers looking to optimize their workday and achieve better balance.

## 🛠️ Tech Stack

- TypeScript monorepo
- NextJS for both app and website
- AWS (Lambda, etc.)
- Terraform for infrastructure management

## 🔗 Learn More

Discover the full power of Increaser at [increaser.org](https://increaser.org)
# 🔐 Auth System with Google & Facebook Login, OTP & Profile Management

A **full-stack authentication system** with an interactive UI.  
Includes **Login/Signup with Google & Facebook**, **OTP verification (Email & Phone)**,  
**Profile update**, **Forgot Password**, **Database authentication**, and a **Welcome Page**.  

---

## 🚀 Features
- ✅ Email/Password Signup & Login  
- ✅ Google OAuth Login  
- ✅ Facebook OAuth Login  
- ✅ Database Authentication (MongoDB/MySQL/Postgres)  
- ✅ OTP Verification  
  - Email OTP (via Nodemailer)  
  - SMS OTP (via Twilio/MSG91)  
- ✅ Forgot Password (Reset link/OTP)  
- ✅ Profile Management  
  - Update Name, Phone, Bio, Profile Picture  
- ✅ Secure Password Hashing (bcrypt/argon2)  
- ✅ JWT Authentication / Session Handling  
- ✅ Responsive Interactive UI (Tailwind + Framer Motion)  
- ✅ Welcome Page with personalized greeting  

---

## 🛠️ Tech Stack
**Frontend**  
- React / Next.js  
- TailwindCSS  
- Framer Motion  

**Backend**  
- Node.js / Express  
- Passport.js / Firebase Auth  
- JWT for Authentication  

**Database**  
- MongoDB / MySQL / PostgreSQL  

**Services**  
- Nodemailer (Email OTP & Reset links)  
- Twilio / MSG91 (Phone OTP)  
- Cloudinary / AWS S3 (Profile Pictures)  

---

📸 Screenshots


🖼️ Welcome Page
![alt text](<Screenshot 2025-10-02 164143.png>)

🖼️ Login Page
![alt text](<Screenshot 2025-10-02 164222.png>)

🖼️ Signup Page with Google/Facebook
![alt text](<Screenshot 2025-10-02 164617.png>)

🖼️ Profile Dashboard
![alt text](<Screenshot 2025-10-02 164308.png>)

🔒 Security

Passwords are hashed using bcrypt/argon2

JWT tokens secured with strong secret key

OTPs expire in 5 minutes

Rate limiting on login attempts

🛡️ Extra Features (Optional)

Dark/Light Mode

Remember Me (persistent login)

Two-Factor Authentication (2FA)

Admin Dashboard for User Management

🤝 Contributing

Pull requests are welcome!
Please fork this repo and submit a PR.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by Vaishnavi ✨