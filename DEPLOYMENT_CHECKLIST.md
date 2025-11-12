# 🚀 Deployment Checklist

Complete this checklist before deploying your Emotion Detection app to production.

---

## 📋 Pre-Deployment Checklist

### 1. Code Preparation
- [ ] All files are present in the project directory
- [ ] `face_emotionModel.h5` is added to the project
- [ ] Model loads successfully in local testing
- [ ] All dependencies in `requirements.txt` are correct
- [ ] Code is tested locally and working

### 2. Configuration Updates
- [ ] Set `debug=False` in `app.py` (line 170)
- [ ] Update `host` and `port` if needed
- [ ] Configure environment variables (if any)
- [ ] Update ALLOWED_EXTENSIONS if needed
- [ ] Set appropriate MAX_CONTENT_LENGTH

### 3. Security Review
- [ ] Debug mode is disabled
- [ ] File upload validation is working
- [ ] Secure filename handling is implemented
- [ ] File size limits are enforced
- [ ] Error messages don't expose sensitive info

### 4. Testing
- [ ] Test with various image formats (JPG, PNG, GIF)
- [ ] Test with images containing faces
- [ ] Test with images without faces
- [ ] Test with invalid file types
- [ ] Test with oversized files
- [ ] Test error handling
- [ ] Test on different browsers
- [ ] Test on mobile devices

---

## 🌐 Platform-Specific Deployment

### Option A: Render (Recommended)

#### Prerequisites
- [ ] GitHub account created
- [ ] Render account created (https://render.com)
- [ ] Code pushed to GitHub repository

#### Steps
1. [ ] Log in to Render dashboard
2. [ ] Click "New +" → "Web Service"
3. [ ] Connect GitHub repository
4. [ ] Configure settings:
   - **Name:** emotion-detection-onipede
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. [ ] Add `gunicorn` to requirements.txt
6. [ ] Deploy and wait for build
7. [ ] Test deployed URL
8. [ ] Update `link_web_app.txt` with URL

#### Additional Files Needed for Render
Create `gunicorn_config.py`:
```python
bind = "0.0.0.0:10000"
workers = 2
```

Update `requirements.txt` to include:
```
gunicorn==21.2.0
```

---

### Option B: Heroku

#### Prerequisites
- [ ] Heroku account created
- [ ] Heroku CLI installed
- [ ] Git repository initialized

#### Steps
1. [ ] Create `Procfile` in project root:
   ```
   web: gunicorn app:app
   ```
2. [ ] Add `gunicorn` to requirements.txt
3. [ ] Login to Heroku: `heroku login`
4. [ ] Create app: `heroku create emotion-detection-onipede`
5. [ ] Deploy: `git push heroku main`
6. [ ] Open app: `heroku open`
7. [ ] Check logs: `heroku logs --tail`
8. [ ] Update `link_web_app.txt` with URL

---

### Option C: PythonAnywhere

#### Prerequisites
- [ ] PythonAnywhere account created
- [ ] Files uploaded to account

#### Steps
1. [ ] Upload all files via Files tab
2. [ ] Open Bash console
3. [ ] Install dependencies: `pip install -r requirements.txt`
4. [ ] Go to Web tab → Add new web app
5. [ ] Choose Flask framework
6. [ ] Configure WSGI file to point to `app.py`
7. [ ] Set working directory
8. [ ] Reload web app
9. [ ] Test URL: `https://yourusername.pythonanywhere.com`
10. [ ] Update `link_web_app.txt` with URL

---

### Option D: Google Cloud Run

#### Prerequisites
- [ ] Google Cloud account
- [ ] gcloud CLI installed
- [ ] Docker installed

#### Steps
1. [ ] Create `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
   ```
2. [ ] Build: `gcloud builds submit --tag gcr.io/PROJECT_ID/emotion-detection`
3. [ ] Deploy: `gcloud run deploy --image gcr.io/PROJECT_ID/emotion-detection`
4. [ ] Test deployed URL
5. [ ] Update `link_web_app.txt` with URL

---

## 📝 Post-Deployment Checklist

### 1. Functionality Testing
- [ ] App loads successfully
- [ ] Upload form is visible
- [ ] Can select and upload images
- [ ] Face detection works
- [ ] Emotion prediction displays
- [ ] Confidence score shows
- [ ] Uploaded image displays correctly
- [ ] Reset button works
- [ ] Error messages display properly

### 2. Performance Testing
- [ ] Page loads in < 3 seconds
- [ ] Image upload is responsive
- [ ] Prediction completes in < 5 seconds
- [ ] No timeout errors
- [ ] Multiple uploads work consecutively

### 3. Cross-Browser Testing
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari
- [ ] Mobile browsers (iOS/Android)

### 4. Responsive Design Testing
- [ ] Desktop (1920x1080)
- [ ] Laptop (1366x768)
- [ ] Tablet (768x1024)
- [ ] Mobile (375x667)

### 5. Documentation Updates
- [ ] Update `link_web_app.txt` with deployed URL
- [ ] Update README.md with deployment info
- [ ] Add screenshots to documentation (optional)
- [ ] Document any deployment issues encountered

---

## 🔧 Troubleshooting Common Issues

### Issue: Model file too large for deployment
**Solution:**
- Use Git LFS (Large File Storage)
- Store model in cloud storage (S3, Google Cloud Storage)
- Load model from URL in app.py

### Issue: App crashes on startup
**Solution:**
- Check logs for error messages
- Verify all dependencies are installed
- Ensure Python version compatibility
- Check file paths are correct

### Issue: Slow prediction times
**Solution:**
- Optimize model (quantization, pruning)
- Use smaller input size
- Implement caching
- Upgrade server resources

### Issue: File upload fails
**Solution:**
- Check file size limits on platform
- Verify UPLOAD_FOLDER permissions
- Ensure static/uploads directory exists
- Check platform storage limits

---

## 📊 Monitoring & Maintenance

### After Deployment
- [ ] Set up error monitoring (Sentry, Rollbar)
- [ ] Configure logging
- [ ] Monitor server resources
- [ ] Track user analytics (optional)
- [ ] Set up uptime monitoring
- [ ] Create backup of model file

### Regular Maintenance
- [ ] Check for dependency updates
- [ ] Monitor error logs weekly
- [ ] Test functionality monthly
- [ ] Update documentation as needed
- [ ] Renew SSL certificates (if applicable)

---

## 🎯 Success Criteria

Your deployment is successful when:
- ✅ App is accessible via public URL
- ✅ All features work as expected
- ✅ No console errors
- ✅ Responsive on all devices
- ✅ Predictions are accurate
- ✅ Error handling works properly
- ✅ Performance is acceptable

---

## 📞 Support Resources

### Platform Documentation
- **Render:** https://render.com/docs
- **Heroku:** https://devcenter.heroku.com/
- **PythonAnywhere:** https://help.pythonanywhere.com/
- **Google Cloud:** https://cloud.google.com/run/docs

### Community Support
- **Stack Overflow:** Tag questions with `flask`, `tensorflow`, `deployment`
- **Reddit:** r/flask, r/learnpython, r/webdev
- **Discord:** Python Discord, Flask Discord

---

## 📝 Final Steps

1. [ ] Complete all checklist items
2. [ ] Test deployed application thoroughly
3. [ ] Update `link_web_app.txt` with final URL
4. [ ] Share link with instructor/peers
5. [ ] Celebrate your successful deployment! 🎉

---

**Deployment Date:** _______________  
**Deployed URL:** _______________  
**Platform Used:** _______________  
**Deployed By:** Onipede - 22CG031936

---

**Good luck with your deployment!** 🚀

