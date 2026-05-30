// ═════════════════════════════════════════════════════════════
// ReviewPro Backend - API آمن ومعالجة CORS
// ═════════════════════════════════════════════════════════════

const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');
require('dotenv').config();

const app = express();

// ── Middleware ──
app.use(express.json({ limit: '10mb' }));
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  credentials: true
}));

// ── تسجيل الطلبات ──
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  next();
});

// ═════════════════════════════════════════════════════════════
// 1. Claude API - توليد التحليلات والردود
// ═════════════════════════════════════════════════════════════
app.post('/api/claude', async (req, res) => {
  try {
    const { system, user, stream } = req.body;
    const apiKey = process.env.ANTHROPIC_API_KEY;

    if (!apiKey) {
      return res.status(500).json({ 
        error: 'مفتاح API لم يتم إعداده على الخادم' 
      });
    }

    if (!system || !user) {
      return res.status(400).json({ 
        error: 'يجب توفير system و user' 
      });
    }

    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: 2000,
        stream: !!stream,
        system,
        messages: [{ role: 'user', content: user }]
      })
    });

    if (!response.ok) {
      const error = await response.json();
      console.error('Claude API Error:', error);
      return res.status(response.status).json({ 
        error: error.error?.message || 'خطأ في Claude API' 
      });
    }

    if (stream) {
      // Streaming response
      res.setHeader('Content-Type', 'text/event-stream');
      res.setHeader('Cache-Control', 'no-cache');
      res.setHeader('Connection', 'keep-alive');
      
      response.body.pipe(res);
    } else {
      // Single response
      const data = await response.json();
      const text = data.content?.[0]?.text || '';
      res.json({ text });
    }

  } catch (error) {
    console.error('Claude endpoint error:', error);
    res.status(500).json({ 
      error: error.message || 'خطأ في معالجة الطلب' 
    });
  }
});

// ═════════════════════════════════════════════════════════════
// 2. Google Maps API - البحث عن العيادات والتقييمات
// ═════════════════════════════════════════════════════════════

// البحث عن عيادة
app.post('/api/google/search', async (req, res) => {
  try {
    const { query, languageCode = 'ar' } = req.body;
    const apiKey = process.env.GOOGLE_MAPS_API_KEY;

    if (!apiKey) {
      return res.status(500).json({ 
        error: 'مفتاح Google Maps لم يتم إعداده' 
      });
    }

    if (!query) {
      return res.status(400).json({ 
        error: 'يجب توفير نص البحث' 
      });
    }

    const response = await fetch('https://places.googleapis.com/v1/places:searchText', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': apiKey,
        'X-Goog-FieldMask': 'places(id,displayName,rating,userRatingCount,formattedAddress,photos)'
      },
      body: JSON.stringify({ 
        textQuery: query,
        languageCode,
        maxResultCount: 5
      })
    });

    if (!response.ok) {
      const error = await response.json();
      console.error('Google Search Error:', error);
      return res.status(response.status).json({ 
        error: error.error?.message || 'خطأ في البحث' 
      });
    }

    const data = await response.json();
    res.json(data);

  } catch (error) {
    console.error('Google search endpoint error:', error);
    res.status(500).json({ 
      error: error.message || 'خطأ في معالجة البحث' 
    });
  }
});

// الحصول على تفاصيل العيادة والتقييمات
app.get('/api/google/place/:placeId', async (req, res) => {
  try {
    const { placeId } = req.params;
    const apiKey = process.env.GOOGLE_MAPS_API_KEY;

    if (!apiKey) {
      return res.status(500).json({ 
        error: 'مفتاح Google Maps لم يتم إعداده' 
      });
    }

    if (!placeId) {
      return res.status(400).json({ 
        error: 'يجب توفير معرّف المكان' 
      });
    }

    const response = await fetch(
      `https://places.googleapis.com/v1/places/${placeId}`,
      {
        headers: {
          'X-Goog-Api-Key': apiKey,
          'X-Goog-FieldMask': 'id,displayName,rating,userRatingCount,reviews,formattedAddress,photos,websiteUri,phoneNumber'
        }
      }
    );

    if (!response.ok) {
      const error = await response.json();
      console.error('Google Details Error:', error);
      return res.status(response.status).json({ 
        error: error.error?.message || 'خطأ في جلب التفاصيل' 
      });
    }

    const data = await response.json();
    
    // تنسيق التقييمات
    const formattedReviews = (data.reviews || []).map(r => ({
      text: r.originalText?.text || r.text?.text || '',
      rating: r.rating || 3,
      author: r.authorAttribution?.displayName || 'مجهول',
      publishTime: r.publishTime,
      rating_count: r.rating
    }));

    // إرجاع البيانات المنسقة
    res.json({
      id: data.id,
      name: data.displayName?.text || '',
      rating: data.rating || 0,
      totalReviews: data.userRatingCount || 0,
      address: data.formattedAddress || '',
      website: data.websiteUri || '',
      phone: data.phoneNumber || '',
      reviews: formattedReviews
    });

  } catch (error) {
    console.error('Google details endpoint error:', error);
    res.status(500).json({ 
      error: error.message || 'خطأ في معالجة الطلب' 
    });
  }
});

// ═════════════════════════════════════════════════════════════
// 3. Health Check
// ═════════════════════════════════════════════════════════════
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// ═════════════════════════════════════════════════════════════
// 4. معالج الأخطاء العام
// ═════════════════════════════════════════════════════════════
app.use((req, res) => {
  res.status(404).json({ error: 'المسار غير موجود' });
});

app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ 
    error: 'خطأ في الخادم',
    message: process.env.NODE_ENV === 'development' ? err.message : undefined
  });
});

// ═════════════════════════════════════════════════════════════
// 5. تشغيل الخادم
// ═════════════════════════════════════════════════════════════
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`
╔═══════════════════���═══════════════════╗
║        ReviewPro Backend Server       ║
║           Running on Port: ${PORT}           ║
╚═══════════════════════════════════════╝
  `);
  console.log('✅ Claude API endpoint: POST /api/claude');
  console.log('✅ Google Search endpoint: POST /api/google/search');
  console.log('✅ Google Details endpoint: GET /api/google/place/:placeId');
  console.log('✅ Health Check: GET /health');
});

module.exports = app;
