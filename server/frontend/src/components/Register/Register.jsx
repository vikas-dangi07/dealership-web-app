import React, { useState } from "react";

export default function Register() {
  const [form, setForm] = useState({ username: "", first_name: "", last_name: "", email: "", password: "" });
  const [message, setMessage] = useState("");
  const update = (event) => setForm({ ...form, [event.target.name]: event.target.value });
  async function submit(event) {
    event.preventDefault();
    setMessage("");
    try {
      const response = await fetch("/djangoapp/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      const data = await response.json();
      setMessage(data.message || (response.ok ? "Registration successful" : "Registration failed"));
    } catch {
      setMessage("Could not contact the server. Please try again.");
    }
  }
  return (
    <main className="register-page">
      <form className="register-card" onSubmit={submit}>
        <h1>Sign-up</h1>
        <label>Username<input name="username" value={form.username} onChange={update} required /></label>
        <label>First Name<input name="first_name" value={form.first_name} onChange={update} required /></label>
        <label>Last Name<input name="last_name" value={form.last_name} onChange={update} required /></label>
        <label>Email<input type="email" name="email" value={form.email} onChange={update} required /></label>
        <label>Password<input type="password" name="password" value={form.password} onChange={update} required minLength={8} /></label>
        <button type="submit">Register</button>
        {message && <p role="status">{message}</p>}
      </form>
    </main>
  );
}
