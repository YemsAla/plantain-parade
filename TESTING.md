# Plantain Parade — Testing

[Return to README](README.md)

## Table of Contents

- [Code Validation](#code-validation)
- [Manual Testing](#manual-testing)
  - [Authentication](#authentication)
  - [Products and Shopping Bag](#products-and-shopping-bag)
  - [Checkout and Payments](#checkout-and-payments)
  - [User Profile](#user-profile)
  - [Product Management](#product-management)
  - [Plantain Ripeness Guide](#plantain-ripeness-guide)
  - [FAQs](#faqs)
- [Bugs and Fixes](#bugs-and-fixes)
- [Known Issues](#known-issues)
- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)

---

## Code Validation

### HTML

| Page | URL | Result |
|------|-----|--------|
| Homepage | `/` | |
| Products | `/products/` | |
| Product Detail | `/products/1/` | |
| Shopping Bag | `/bag/` | |
| Checkout | `/checkout/` | |
| Profile | `/profile/` | |
| Plantain Ripeness Guide | `/ripeness-guide/` | |
| FAQs | `/faqs/` | |

### CSS

| File | Result |
|------|--------|
| base.css | |
| profile.css | |

### JavaScript

| File | Result |
|------|--------|
| stripe_elements.js | |
| countryfield.js | |

### Python (PEP8)

| File | Result |
|------|--------|
| checkout/views.py | |
| checkout/models.py | |
| checkout/webhook_handler.py | |
| profiles/views.py | |
| profiles/models.py | |
| products/views.py | |
| products/models.py | |
| bag/contexts.py | |
| plantain_ripeness_guide/views.py | |
| plantain_ripeness_guide/models.py | |
| faqs/views.py | |
| faqs/models.py | |

---

## Manual Testing

### Authentication

| Test | Expected Result | Actual Result | Pass/Fail |
|------|----------------|---------------|-----------|
| Register with valid credentials | Redirected to homepage with success message | | |
| Register with mismatched passwords | Error message shown | | |
| Register with existing username | Error message shown | | |
| Login with valid credentials | Redirected to homepage, nav updates | | |
| Login with wrong password | Error message shown, stays on login page | | |
| Logout | Redirected to homepage, nav shows Login/Register | | |
| Access profile page when logged out | Redirected to login page | | |
| Access product management when not superuser | Redirected with error message | | |

---

### Products and Shopping Bag

| Test | Expected Result | Actual Result | Pass/Fail |
|------|----------------|---------------|-----------|
| Browse all products | All products display as cards | | |
| Filter by category (Rum) | Only rum products shown | | |
| Sort by price low to high | Products reorder correctly | | |
| Sort by rating | Products reorder correctly | | |
| Search by keyword | Matching products shown | | |
| Search with no results | "0 products found" message shown | | |
| View product detail | Full detail page loads | | |
| Add product to bag | Success toast shows with bag contents | | |
| Adjust quantity in bag | Quantity updates, totals recalculate | | |
| Remove item from bag | Item removed, totals update | | |
| Empty bag | Message shown, no checkout button | | |

---

### Checkout and Payments

| Test | Expected Result | Actual Result | Pass/Fail |
|------|----------------|---------------|-----------|
| Checkout with valid card (4242 4242 4242 4242) | Order placed, redirected to success page | | |
| Checkout with invalid card | Error message shown below card field | | |
| Checkout with empty form fields | Validation errors shown | | |
| Logged in user checkout | Form pre-filled with profile data | | |
| Save info checkbox checked | Profile updated with checkout details | | |
| Order confirmation page loads | Order number, items and totals shown | | |
| Confirmation email received | Email printed to console in dev | | |
| Webhook payment_intent.succeeded | 200 response in Stripe terminal | | |

---

### User Profile

| Test | Expected Result | Actual Result | Pass/Fail |
|------|----------------|---------------|-----------|
| View profile page | Delivery form and order history shown | | |
| Update delivery information | Success message, form saves | | |
| View order history | Past orders shown in table | | |
| Click order number in history | Past order confirmation page loads | | |
| Info toast on past order page | Message shown without bag contents | | |

---

### Product Management (Superuser only)

| Test | Expected Result | Actual Result | Pass/Fail |
|------|----------------|---------------|-----------|
| Product Management link visible to superuser | Link appears in My Account dropdown | | |
| Product Management link hidden from regular users | Link not visible | | |
| Add a product | Product saved, redirected to product detail | | |
| Add product with invalid price | Validation error shown | | |
| Edit a product | Form pre-filled, updates on save | | |
| Delete a product | Product removed, redirected to products | | |
| Non-superuser accesses /products/add/ directly | Redirected with error message | | |

---

### Plantain Ripeness Guide

| Test | Expected Result | Actual Result | Pass/Fail |
|------|----------------|---------------|-----------|
| View ripeness guide | All stages shown as cards | | |
| Click Learn More | Detail page loads with correct content | | |
| Best uses and cooking tips show as bullet points | Bullet list renders correctly | | |
| Add stage (superuser) | Stage saved, redirected to guide | | |
| Edit stage (superuser) | Form pre-filled, updates on save | | |
| Delete stage (superuser) | Confirmation page shown, then deleted | | |
| Add/Edit/Delete links hidden from regular users | Links not visible | | |
| Non-superuser accesses /ripeness-guide/add/ directly | Redirected with error message | | |

---

### FAQs

| Test | Expected Result | Actual Result | Pass/Fail |
|------|----------------|---------------|-----------|
| View FAQs page | Accordion with categories shown | | |
| Click category header | Accordion opens/closes | | |
| Add FAQ (superuser) | FAQ saved, success toast without bag | | |
| Edit FAQ (superuser) | Form pre-filled, updates on save | | |
| Delete FAQ (superuser) | Confirmation page shown, then deleted | | |
| Add/Edit/Delete buttons hidden from regular users | Buttons not visible | | |
| Non-superuser accesses /faqs/add/ directly | Redirected with error message | | |

---

## Bugs and Fixes

| Bug | Fix |
|-----|-----|
| `.venv` folder committed to GitHub causing Heroku build failure | Ran `git rm --cached -r .venv/` and added `.venv/` to `.gitignore` |
| `crispy_bootstrap4` module not found on Heroku | Installed `crispy-bootstrap4` and added to `requirements.txt` and `INSTALLED_APPS` |
| Profile form fields not rendering with `{{ form\|crispy }}` | Installed `crispy-bootstrap4` package which is required separately in newer versions |
| Stripe webhook returning 500 on `payment_intent.succeeded` | Fixed typo `request.user.usdername` → `request.user.username` in `cache_checkout_data` |
| `UserProfile.DoesNotExist` error in webhook handler | Changed `UserProfile.objects.get()` to `UserProfile.objects.get_or_create()` |
| Delete confirmation not showing before deleting ripeness stage | Changed delete link from `<a>` tag to a `<form method="GET">` so it hits the view as GET before POST |
| Success toast showing bag contents on FAQs page | Added `on_faqs_page: True` to FAQs view context and updated toast condition |
| Success toast showing bag contents on profile page | Added `on_profile_page: True` to profile view context and updated toast condition |
| AWS S3 collectstatic returning 403 HeadObject error | `DISABLE_COLLECTSTATIC=1` set as temporary workaround — see Known Issues |
| Django 6 incompatibility with `django-countries 7.2.1` | Upgraded to `django-countries 7.6.1` |

---

## Known Issues

| Issue | Notes |
|-------|-------|
| Static files not served via S3 on Heroku | Django 6 removed `STATICFILES_STORAGE` setting used in CI walkthrough. `DISABLE_COLLECTSTATIC=1` set as workaround. Site is functional but unstyled on Heroku. To be resolved before final submission. |
| Stripe webhook secret not configured on Heroku | `STRIPE_WH_SECRET` not yet added to Heroku config vars. Payments work but webhook fallback not active on deployed site. |
| Overripe plantain image missing | Ran out of image credits during development. Default no-image placeholder displays. |

---

## Responsiveness

Tested across mobile (375px), tablet (768px) and desktop (1440px).

| Breakpoint | Result |
|-----------|--------|
| Mobile (375px) | Navbar collapses to hamburger. Products stack to single column. Checkout form stacks. |
| Tablet (768px) | Navbar collapses to hamburger. Products show 2 columns. |
| Desktop (1440px+) | Full nav visible. Products show 4 columns. Two-column checkout layout. |

---

## Browser Compatibility

| Browser | Result | Notes |
|---------|--------|-------|
| Chrome | | |
| Edge | | |
| Firefox | | |
| Safari | | |

---

[Return to README](README.md)