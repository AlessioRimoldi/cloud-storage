import type { Metadata } from "next";
import { inter } from "@/app/ui/fonts";
import "./globals.css";

export const metadata: Metadata = {
  title: "Cloud Research Platform",
  description: "Cloud platform to perform research",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.className} antialiased`}>{children}</body>
    </html>
  );
}
